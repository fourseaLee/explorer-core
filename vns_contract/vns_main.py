import time
from vns_web3 import Web3, HTTPProvider
import vns_params
import vns_db
import vns_web3parse
import vns_kafka
import json
import logging
configuer_file = 'configure.json'
params = vns_params.readParams(configuer_file)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
filter_handler = logging.FileHandler('test.log', mode = 'w')
filter_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
filter_handler.setFormatter(formatter)
logger.addHandler(filter_handler)
    
def updateOffset(offset):
    #sql = "INSERT INTO `blockscan`.`kafka_offset` (`offset`, `name`) VALUES ('%d', '%s');" % (offset, params['consumertopic'])
    sql = "UPDATE `kafka_offset` SET `offset`='%d' WHERE  `name`='%s';" % (offset, params['consumertopic'])
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    vns_db.flushDB(mysql_url, mysql_name, mysql_password, mysql_db,sql)

def addContact(dict_data):
    sql = "INSERT INTO `contract_detail` (`name`, `symbol`, `contract`, `total`, `decimal`, `standard`) VALUES ('%s', '%s', '%s', '%s', '%d', '%s');" % (dict_data['name'],dict_data['symbol'],dict_data['contract'],dict_data['total'],dict_data['decimal'],dict_data['tokenStandard'])
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    vns_db.flushDB(mysql_url, mysql_name, mysql_password, mysql_db,sql)

def getContract(contract_address):
    results = {}    
    sql = "SELECT `name`, `symbol` ,`decimal`,`standard`  FROM contract_detail WHERE  `contract`= '%s';" % (contract_address)
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    results = vns_db.getData(mysql_url, mysql_name, mysql_password, mysql_db,sql)
    return results

def getTokenStandard(standard):
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    sql = "SELECT `offset` FROM kafka_offset WHERE `name` = 'VNSContract' order by id desc  limit 1;"
    offset_result = vns_db.getData(mysql_url, mysql_name, mysql_password, mysql_db,sql)
    offset_contract = offset_result[0][0]
    consumerLoop(offset_contract)
   
def processMsg(msg):
    producer_url = params['producerurl']
    producer_topic = params['producertopic']
    json_msg = json.loads(msg)
    
    input_data = json_msg['input']
    print(json_msg)
    address_from = json_msg['from']
    contract_to = json_msg['to']
    
    if contract_to:
        #check contract type
        dict_data = vns_web3parse.parseInputAction(input_data)
        if dict_data:
            dict_data['hash'] = json_msg['hash']
            dict_data['blockNumber'] = json_msg['blockNumber']
            dict_data['contract']  = contract_to
            dict_data['from'] = address_from 
            contract_data = getContract(contract_to)
            if contract_data:
                dict_data['name'] = contract_data[0][0]
                dict_data['symbol'] = contract_data[0][1]
                dict_data['decimal'] = contract_data[0][2]
                dict_data['tokenStandard'] = contract_data[0][3]
            else:
                dict_data['name'] = 'name'
                dict_data['symbol'] = 'symbol'
                dict_data['decimal'] = 0
            print(dict_data)
            json_data = json.dumps(dict_data) 
            vns_kafka.pushProducer(producer_url, producer_topic, json_data.encode())
        else:
            logger.info(json_msg)

    else:
        dict_data = vns_web3parse.parseInputCreate(input_data)
        nonce = json_msg['nonce']
        contract_address = vns_web3parse.getContractAddress(address_from, nonce) 
        #print(dict_data)
        if dict_data:
            dict_data['asset'] = 'VNS'
            dict_data['hash'] = json_msg['hash']
            dict_data['blockNumber'] = json_msg['blockNumber']
            dict_data['contract']  = contract_address
            #dict_data['tokenStandard'] = 'VRC20'
            dict_data['tokenAction'] = 'create'
            dict_data['from'] = address_from
            dict_data['to'] = ''
            json_data = json.dumps(dict_data)
            #print(type(json_data))
            #print(json_data)
            addContact(dict_data)
            vns_kafka.pushProducer(producer_url, producer_topic, json_data.encode())
        else:
            logger.info(json_msg)



def callbackConsumer(msg):
    print('\n')
    if msg:
        #print(msg)
        updateOffset(msg.offset)
        print('\n')
        json_value = json.loads(msg.value)
        processMsg(msg.value)

def consumerLoop(offset):
    consumer_url = params['consumerurl']
    consumer_topic = params['consumertopic']
    vns_kafka.syncConsumer(consumer_url, offset, consumer_topic, callbackConsumer)

def main():
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    sql = "SELECT `offset` FROM kafka_offset WHERE `name` = '%s' order by id desc  limit 1;" % (params['consumertopic'])
    offset_result = vns_db.getData(mysql_url, mysql_name, mysql_password, mysql_db,sql)
    print(offset_result)
    offset_contract = offset_result[0][0]

    print(offset_contract)
    consumerLoop(offset_contract)



if __name__ == '__main__':
    main()
