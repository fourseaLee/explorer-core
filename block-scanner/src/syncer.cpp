#include <thread>
#include <chrono>
#include "common.h"
#include "syncer.h"
#include "producer.h"
#include "db_mysql.h"
#include <unistd.h>
#include <glog/logging.h>

CSyncer g_syncer;

CSyncer::CSyncer()
{
}

CSyncer::~CSyncer()
{
}

bool CSyncer::addBlockRpc(BlockChainRpc *block_rpc)
{
    vect_blockchain_.push_back(block_rpc);
    return true;
}

/**
 * SyncBlocks - sync new blocks from full node
 *
 */
void CSyncer:: syncBlocks()
{
    //usleep(1000);


    bool ret = false;
    while (true)
    {
        try
        {
            BlockChainRpc* chain_rpc = NULL;
            uint  block_chain_size = vect_blockchain_.size();
            if(!g_run_syncer)
            {
                break;
            }
            usleep(1000);

            uint64_t block_cout = 0;
            for(uint i = 0; i < block_chain_size; i++)
            {
                Asset *asset = NULL;
                chain_rpc = vect_blockchain_[i];
                chain_rpc->getAsset(asset);
                ret = chain_rpc->getBlockCount(block_cout);
                if (asset->height >= block_cout || !ret )
                {
                    continue;
                }

                std::string block_detail;
                std::cout << "block cout:" <<  block_cout << std::endl;
                for(; asset->height <= block_cout; ++asset->height)
                {
                    chain_rpc->getBlockDetail(asset->height, block_detail);
                    chain_rpc->PushKakfaData(block_detail);
                    std::vector<std::string> vect_txid;
                    chain_rpc->getBlockTxids(block_detail,vect_txid);
                    std::string tx_detail;
                    for(uint j = 0; j < vect_txid.size(); j++)
                    {
                        chain_rpc->getTransaction(vect_txid[j], tx_detail);
                        chain_rpc->PushKakfaData(tx_detail);
                    }

                    if( asset->height % 1000 == 0 || asset->height == block_cout)
                        UpdateBlockHeight(asset);
                }
            }
        }
        catch(...)
        {
            LOG(ERROR) << "catch  a bug";
            usleep(10000000);
        }
    }
}

bool CSyncer::UpdateBlockHeight(Asset *asset)
{
    std::string sql = "update asset_desc set height=" + std::to_string(asset->height)
            + " where name = '" + asset->name + "';";
    return g_db_mysql->ExecuteSql(sql);
}

