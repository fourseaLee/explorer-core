#include "init.h"
#include "common.h"
#include <glog/logging.h>
#include <unistd.h>
#include "db_mysql.h"
#include <boost/program_options.hpp>
#include  "blockchain_rpc.h"
#include "syncer.h"
#include "vns_rpc.h"

static ConfManager s_conf;
static bool InitLog(const std::string& log_path)
{
    FLAGS_alsologtostderr = false;
    FLAGS_colorlogtostderr = true;
    FLAGS_max_log_size = 100;
    FLAGS_stop_logging_if_full_disk  = true;
    std::string log_exec = "log_exe";
    google::InitGoogleLogging(log_exec.c_str());
    FLAGS_log_dir = log_path;
    std::string log_dest = log_path+"/info_";
    google::SetLogDestination(google::GLOG_INFO,log_dest.c_str());
    log_dest = log_path+"/warn_";

    google::SetLogDestination(google::GLOG_WARNING,log_dest.c_str());
    log_dest = log_path+"/error_";
    google::SetLogDestination(google::GLOG_ERROR,log_dest.c_str());
    log_dest = log_path+"/fatal_";
    google::SetLogDestination(google::GLOG_FATAL,log_dest.c_str());
    google::SetStderrLogging(google::GLOG_ERROR);
    google::InstallFailureSignalHandler();

    return true;
}

bool ParseCmd(int argc,char*argv[])
{
    std::cout << "Parse cmd ------------------------------------------------";
    using namespace boost::program_options;
    std::string path_configure ;
    std::string path_log;
    boost::program_options::options_description opts_desc("All options");
    opts_desc.add_options()
            ("help,h", "help info")
            ("log_path,l", value<std::string>(&path_log)->default_value("../log"), "log configure ")
            ("configure_path,c", value<std::string>(&path_configure)->default_value("../conf/server_main.conf"), "path configure ");

    variables_map cmd_param_map;
    try
    {
        store(parse_command_line(argc, argv, opts_desc), cmd_param_map);
    }
    catch(boost::program_options::error_with_no_option_name &ex)
    {
        std::cout << ex.what() << std::endl;
    }
    notify(cmd_param_map);
    
    if (cmd_param_map.count("help"))
    {
        std::cout << opts_desc << std::endl;
        return false;
    }

    InitLog(path_log);
    s_conf.setConfPath(path_configure);
    s_conf.readConfigFile();
    s_conf.printArg();
    return true;
}

bool InitDB()
{
    LOG(INFO) << "Init db ------------------------------------------------";
    DBMysql::MysqlConnect* connect = new DBMysql::MysqlConnect();
    connect->use_db = s_conf.getArgs("mysqldb", "api_tran");
    connect->user_pass = s_conf.getArgs("mysqlpass", "a");
    connect->port = std::atoi(s_conf.getArgs("mysqlport", "3306").c_str());
    connect->user_name = s_conf.getArgs("mysqluser", "snort");
    connect->url = s_conf.getArgs("mysqlserver", "192.168.0.18");
    g_db_mysql->SetConnect(connect);
    return g_db_mysql->OpenDB();
}

static BlockChainRpc* CreateBlockRpc(Asset* asset)
{
    BlockChainRpc* block_rpc = NULL;
    if(asset->name == "VNS")
    {
        block_rpc = new VNSRpc();
        block_rpc->setAsset(asset);
        if ( !block_rpc->createKafkaProducer() )
        {
            std::cout << "init " << asset->name << " url" << asset->kafka_url << "failed!" << std::endl;
            assert(false);
        }
        return  block_rpc;
    }

}

static CSyncer  s_syncer;
bool InitAsset()
{
    LOG(INFO) << "Init asset -----------------------------------------------------";
    std::string select_sql = "select id,name,kafka_url,node_url,wallet_url,auth,height from asset_desc order by id";

    DBMysql::JsonDataFormat json_format;
    json_format.column_size = 7;
    json_format.map_column_type[0] = DBMysql::INT;
    json_format.map_column_type[1] = DBMysql::STRING;
    json_format.map_column_type[2] = DBMysql::STRING;
    json_format.map_column_type[3] = DBMysql::STRING;
    json_format.map_column_type[4] = DBMysql::STRING;
    json_format.map_column_type[5] = DBMysql::STRING;
    json_format.map_column_type[6] = DBMysql::INT;

    json json_data;
    bool ret = g_db_mysql->GetDataAsJson(select_sql, &json_format, json_data);

    if (!ret)
    {
        LOG(ERROR) << "init asset from db fail.";
        return false;
    }
    LOG(INFO) << "asset info : " << json_data.dump();

    for (uint i = 0; i < json_data.size(); ++i)
    {
        json json_value = json_data.at(i);
        /*coin_id,name,short_name,rpc_url,branch,auth,height,least_confimation,wallet_url*/
        Asset* asset = new Asset();
        std::cout << json_value.dump() << std::endl;
        for(uint j = 0; j < json_format.column_size; ++j)
        {
            switch(j)
            {
            case 0:
                asset->id = json_value.at(j).get<uint>();
                break;
            case 1:
                asset->name = json_value.at(j).get<std::string>();
                break;
            case 2:
                asset->kafka_url = json_value.at(j).get<std::string>();
                break;
            case 3:
                asset->rpc_node_url = json_value.at(j).get<std::string>();
                break;
            case 4:
                asset->rpc_wallet_url = json_value.at(j).get<std::string>();
                break;
            case 5:
                asset->auth = json_value.at(j).get<std::string>();
                break;
            case 6:
                asset->height = json_value.at(j).get<uint64_t>();
                break;
            default:
                break;
            }
        }
        BlockChainRpc* block_rpc = CreateBlockRpc(asset);
        s_syncer.addBlockRpc(block_rpc);
    }
    return true;
}


static void SignalHandler(int sig)
{
    switch (sig)
    {
    case SIGTERM:
    case SIGHUP:
    case SIGQUIT:
    case SIGINT:
    {
        LOG(ERROR) << "recieve an assert signal " << sig;
        g_run_syncer = false;
    }
        break;
    }
}

void startScan()
{
    signal(SIGHUP, SignalHandler);
    signal(SIGTERM, SignalHandler);
    signal(SIGINT, SignalHandler);
    signal(SIGQUIT, SignalHandler);

    /*if (daemon(1, 0))
    {
        std::cout  << "daemon failed" << std::endl;
        return ;
    }*/

    s_syncer.syncBlocks();
}
