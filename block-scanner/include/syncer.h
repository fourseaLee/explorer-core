#ifndef SYNCER_H
#define SYNCER_H
#include <iostream>
#include <vector>
#include <map>
#include "blockchain_rpc.h"
#include <mutex>

class CSyncer
{
public:
    CSyncer();
    ~CSyncer();

public:
    bool addBlockRpc(BlockChainRpc* block_rpc);

public:
    void syncBlocks();

protected:
    bool UpdateBlockHeight(Asset* asset);

protected:
    std::vector<BlockChainRpc*> vect_blockchain_;
};


#endif
