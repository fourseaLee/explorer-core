#include "vns_rpc.h"
#include <glog/logging.h>
#include <exception>

bool VNSRpc::getBlockCount(uint64_t &height)
{
    json json_params = json::array();
    json json_post;
    structRpcMethodParams("vns_blockNumber",json_params,json_post);

    std::string response;
    if ( !CurlRpcNode(json_post.dump(),response) )
    {
        LOG(ERROR) <<response;
        NodeError();
        throw std::runtime_error("get block count has no effect");
        return false;
    }
    json json_response = json::parse(response);

    std::string block_cout_hex = json_response["result"].get<std::string>();
    std::string block_cout_dec = HexToDec(block_cout_hex);
    height = std::atol(block_cout_dec.c_str());
    return true;

}

bool VNSRpc::getBlockDetail(const uint64_t &height, std::string &block_detail)
{
    //'{"jsonrpc":"2.0","method":"vns_getBlockByNumber","params":["0x23",true],"id":1}'

    json json_params = json::array();
    std::string height_hex  = DecToHex(height);
    json_params.push_back(height_hex);
    json_params.push_back(true);
    json json_post;
    structRpcMethodParams("vns_getBlockByNumber",json_params,json_post);
    std::string response;
    if ( !CurlRpcNode(json_post.dump(),response) )
    {
        LOG(ERROR) << response;
        NodeError();

        throw std::runtime_error("get block detail has no effect");
        return false;
    }

    block_detail = response;

}

bool VNSRpc::getBlockTxids(const std::string &block_detail, std::vector<std::string> &vect_txid)
{
    json json_block = json::parse(block_detail);
    json json_result = json_block["result"];

    json json_tx = json_result["transactions"];
    for(uint i = 0; i < json_tx.size(); i++)
    {
        if (json_tx.at(i)["hash"].is_null())
            continue;

        std::string input = json_tx.at(i)["input"].get<std::string>();
      
        if (json_tx.at(i)["to"].is_null() || input != "0x")
        {
            LOG(INFO) << "contract transaction:";
            std::string contract_transaction = json_tx.at(i).dump();
            LOG(INFO) << contract_transaction;

            int ret = kafka_producer_contract_->pushData(contract_transaction);
            LOG(INFO) << "constract transaction ret: " << ret;
        }

        std::string txid = json_tx.at(i)["hash"].get<std::string>();
        vect_txid.push_back(txid);
    }

    return true;
}

bool VNSRpc::getTransaction(const std::string &txid, std::string &tx_detail)
{
    json json_params = json::array();
    json_params.push_back(txid);
    json json_post;
    structRpcMethodParams("vns_getTransactionReceipt",json_params,json_post);
    std::string response;
    if ( !CurlRpcNode(json_post.dump(),response) )
    {
        LOG(ERROR) << response;        
        NodeError();

        throw std::runtime_error("get transaction  has no effect");
        return false;
    }
    tx_detail = response;
    return true;

}

bool VNSRpc::structRpcMethodParams(const std::string rpc_method, const json &json_params, json &json_post)
{
    json_post["jsonrpc"] = "2.0";
    json_post["method"] = rpc_method;
    json_post["params"] = json_params;
    json_post["id"] = 1;
    return true;
}
