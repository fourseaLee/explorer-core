#ifndef __COMMON_H__
#define __COMMON_H__

#include <string>
#include <vector>
#include <map>
#include <gmpxx.h>
#include <gmp.h>
#include "json.hpp"
#include "producer.h"

using json = nlohmann::json;

class ConfManager
{
public:
    ConfManager(std::string path = "../conf/server_main.conf"):path_(path)
    {
    }
    ~ConfManager(){}
    std::string getArgs(const std::string& strArg, const std::string& strDefault);
    bool isArgSet(const std::string& strArg);
    void setConfPath(std::string path)
    {
        path_ = path;
    }
    void printArg();
    void readConfigFile();

private:
    void readConfJsonObj(const json js);
private:
    std::string path_;
    json conf_;
    std::map<std::string,std::string> mapArgs_;
};

extern std::unique_ptr<ConfManager>confptr;
extern ProducerKafka* g_kafka_producer;
extern std::map<std::string,int> g_map_coin_coinid;
extern std::map<int,std::string> g_map_coinid_coin;
extern bool g_run_syncer;
struct CurlParams
{
    std::string url;
    std::string auth;
    std::string data;
    std::string content_type;
    CurlParams()
    {
        content_type = "content-type:application/json";
    }
};
bool CurlPost(const std::string& url, const std::string& data,
              const std::string& auth, std::string& response);
bool CurlPostParams(const CurlParams& params, std::string& response);

//big_int_num 是大整数， div_e_pow是除以e（10）的幂次，precise是精确位数，precise_float 是返回的浮点数
bool BigIntToPreciseFloat(const std::string& big_int_num,int div_e_pow ,int precise,std::string& precise_float);

std::string HexToDec(const std::string &hex);
std::string DecToHex(const uint64_t height);
#endif
