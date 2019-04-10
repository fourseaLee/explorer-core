
#include "blockchain_rpc.h"
#include <glog/logging.h>


void BlockChainRpc::setAsset( Asset *asset)
{
    asset_ = asset;
}

void BlockChainRpc::getAsset( Asset*& asset)
{
    asset = asset_;
}

bool BlockChainRpc::createKafkaProducer()
{
    if (PRODUCER_INIT_SUCCESS !=kafka_producer_->init_kafka(0, asset_->kafka_url.c_str(), asset_->name.c_str()))
    {
        return false;
    }
    
    std::string topic_name = asset_->name + "Contract1";
    if (PRODUCER_INIT_SUCCESS !=kafka_producer_contract_->init_kafka(0, asset_->kafka_url.c_str(), topic_name.c_str()))
    {
        return false;
    }
    return true;
}



bool BlockChainRpc::CurlRpcWallet(const std::string &post_data, std::string &response)
{
    return CurlPost(asset_->rpc_wallet_url,post_data,asset_->auth,response);
}

int BlockChainRpc::PushKakfaData(const std::string &kafka_msg)
{
    return kafka_producer_->pushData(kafka_msg);
}

void BlockChainRpc::NodeError()
{
    LOG(ERROR) << "FULL NODE  ERROR" ;
    LOG(ERROR) << "asset name: " << asset_->name ;
    LOG(ERROR) << "node url: " << asset_->rpc_node_url;
    LOG(ERROR) << "wallet url: " << asset_->rpc_wallet_url;
}

bool BlockChainRpc::CurlRpcNode(const std::string &post_data, std::string &response)
{
    return CurlPost(asset_->rpc_node_url,post_data,asset_->auth,response);
}
