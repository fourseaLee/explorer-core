#ifndef BLOCKCHAIN_RPC_H
#define BLOCKCHAIN_RPC_H
#include "common.h"
#include <iostream>
#include "producer.h"

struct Asset
{
    uint id;
    std::string name;//kafka topic name (asset short name)
    std::string kafka_url;
    std::string rpc_node_url;
    std::string rpc_wallet_url;
    std::string auth;
    uint64_t height;
    Asset():id(0),height(0)
    {
    }
    virtual ~Asset()
    {

    }
};

struct Token : public Asset
{  
    std::string address;
    uint16_t decimals;
    Token():decimals(0)
    {}
    virtual ~Token()
    {}
};

class BlockChainRpc
{
public:
    BlockChainRpc()
    {
        kafka_producer_ = new ProducerKafka();
        kafka_producer_contract_ = new ProducerKafka();
    }

    virtual ~BlockChainRpc()
    {
        delete kafka_producer_;
	delete kafka_producer_contract_;
    }

public:
    void setAsset(Asset *asset);
    void getAsset(Asset *& asset);

    bool createKafkaProducer();

public:
    virtual bool getBlockCount(uint64_t& height)
    {
        return true;
    }

    virtual bool getBlockDetail( const uint64_t& height, std::string& block_detail)
    {
        return true;
    }
    virtual bool getBlockTxids(const std::string& block_detail, std::vector<std::string>& vect_txid)
    {
        return true;
    }

    virtual bool getTransaction(const std::string& txid, std::string& tx_detail)
    {
        return true;
    }

public:
    virtual bool CurlRpcNode(const std::string& post_data,std::string& response);

    virtual bool CurlRpcWallet(const std::string& post_data,std::string& response);

    virtual int PushKakfaData(const std::string& kafka_msg);

public:
    void NodeError();

protected:
    Asset* asset_;
    ProducerKafka* kafka_producer_;
    ProducerKafka* kafka_producer_contract_;
};

#endif // BLOCKCHAIN_RPC_H
