#include <iostream>
#include <thread>
#include "init.h"
#include "syncer.h"
#include <unistd.h>

int test()
{
   //  Asset* asset = new Asset();
   //  asset->auth = "test:test";
   //  asset->branch = 6;
   //  asset->coin_id = 500;
   //  asset->least_confimation = 10;
   //  asset->rpc_node_url = "http://47.52.74.14:8081/json_rpc";
   //  asset->rpc_wallet_url = "http://192.168.0.68:8070/json_rpc";
   //  asset->short_name = "BCN";
   //  // BCNRpc bcnrpc;
   //  asset->height = 1710754;
   //  bcnrpc.setAsset(asset);

   //  uint64_t block_height = 0;
   //  bcnrpc.getBlockCount(block_height);
   //  std::cout << "block height: " << block_height << std::endl;

   //  std::string hash;
   //  bcnrpc.getBlockHash(1710805,hash);
   //  std::cout << "block hash: " << hash << std::endl;

   //  std::vector<TxBase> vect_tx_detail;
   //  bcnrpc.getTransaction(block_height,vect_tx_detail);

   //  for (uint i=0; i < vect_tx_detail.size(); i++)
   //  {
   //      std::cout << std::endl << std::endl << std::endl;
   //      TxBase tx = vect_tx_detail.at(i);
   //      std::cout << "from: " <<tx.address_from << std::endl;
   //      std::cout << "txid: " <<tx.txid << std::endl;
   //      std::cout << "height: " <<tx.block_height << std::endl;
   //      std::cout << "time: " << tx.time << std::endl;
   //      std::cout << "address: " << tx.map_addressto_amount.begin()->first << "amount: " << tx.map_addressto_amount.begin()->second << std::endl;
   //      std::cout << "confirm: " <<tx.confirm << std::endl;
   //  }
}

int main(int argc,char*argv[])
{
    if (!ParseCmd(argc, argv)) 
    {
        std::cout << "Parse cmd failed !" << std::endl;
        return 0;
    }

    if (!InitDB())
    {
        std::cout << "Init DB failed !" << std::endl;
        return 0;
    }

    if (!InitAsset())
    {   
        std::cout << "Init asset failed !" << std::endl;
        return 0;
    }

    startScan();

   return 0;
}
