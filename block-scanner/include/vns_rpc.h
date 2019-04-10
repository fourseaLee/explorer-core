#ifndef VNS_RPC_H
#define VNS_RPC_H
#include "blockchain_rpc.h"

class VNSRpc:public BlockChainRpc
{
public:
    VNSRpc()
    {}
    virtual ~VNSRpc()
    {}

public:
    bool getBlockCount(uint64_t& height);

    bool getBlockDetail( const uint64_t& height, std::string& block_detail);

    bool getBlockTxids(const std::string& block_detail, std::vector<std::string>& vect_txid);

    bool getTransaction(const std::string& txid, std::string& tx_detail);
protected:
    bool structRpcMethodParams(const std::string rpc_method,const json& json_params,json& json_post);

};

#endif // VNS_RPC_H
