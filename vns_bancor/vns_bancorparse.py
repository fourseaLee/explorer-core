import time
import vns_params
import vns_web3parse
import vns_bancor
import getopt
import sys
   
def main():
   etherToken = vns_bancor.getEtherToken()
   
   vns_bancor.web3.personal.unlockAccount(account=vns_bancor.web3.vns.defaultAccount, passphrase='vns_mnemonic' )
   tx_hash = etherToken.deploy(transaction={'from':vns_bancor.web3.vns, 'gas': 410000})
   print(tx_hash)

   vns_bancor.web3.personal.lockAccount(account=web3.vns.defaultAccount)

def getContractType(txinput):
    
    
