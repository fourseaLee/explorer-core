import time
from vns_web3 import Web3, HTTPProvider
import vns_params
import vns_db
import vns_web3parse
import vns_kafka
import json
import vns_codeabi

configuer_file = 'configure.json'
params = vns_params.readParams(configuer_file)
logger = vns_params.initLogger('bancor.log')
vns_bancor_rule = ()
vns_web3_fn = ()
producer_url = params['producerurl']
producer_topic = params['producertopic']


def execSql(sql,flushdb=False):
    mysql_url = params['mysqlurl']
    mysql_name = params['mysqlname']
    mysql_password = params['mysqlpassword']
    mysql_db = params['mysqldb']
    if flushdb:
        vns_db.flushDB(mysql_url, mysql_name, mysql_password, mysql_db,sql)
        return None
    else: 
        results = vns_db.getData(mysql_url, mysql_name, mysql_password, mysql_db,sql)
        return results
 

def updateOffset(offset):
    sql = "UPDATE `kafka_offset` SET `offset`='%d' WHERE  `name`='%s';" % (offset, params['consumertopic'])
    execSql(sql,True)


def flushContractToDB(dict_data, create = False):
    if create:
        sql1 = "INSERT INTO `contract` (`issuer`, `contractaddress`, `contractname`) VALUES ('%s', '%s', '%s');" % (dict_data['from'],dict_data['contract'],dict_data['name'])    
        execSql(sql1,True)
        sql = "INSERT INTO `content` (`contractaddress`, `from`,`input`, `type`, `action`) VALUES ('%s', '%s', '%s', '%d', '%s');" % (dict_data['contract'], dict_data['from'], "create", int(dict_data['type']), dict_data['action'])
        execSql(sql,True)
    else:
        sql = "INSERT INTO `content` (`contractaddress`, `from`,`input`, `type`, `action`) VALUES ('%s', '%s', '%s', '%d', '%s');" % (dict_data['contract'], dict_data['from'], dict_data['input'], int(dict_data['type']), dict_data['action'])
        execSql(sql, True)

def getBancorVnsWeb3Fn():
    sql = "select `fnname`, `fnweb3` from  fnweb3 ;"
    return execSql(sql, True)


def processMsg(msg):
    producer_url = params['producerurl']
    producer_topic = params['producertopic']
    json_msg = json.loads(msg)
    input_data = json_msg['input']
    address_from = json_msg['from']
    contract_to = json_msg['to']
    dict_data = {}
    dict_data['hash'] = json_msg['hash']
    dict_data['from'] = address_from 
    #dict_data['input'] = input_data

    #print(address_from)        

    if contract_to:
        #check contract type
        ret = vns_web3parse.parseBancorAction(input_data, vns_web3_fn, dict_data)
        dict_data['contract'] = contract_to
        dict_data['action'] = 'run'
        dict_data['type'] = '1'
        dict_data['input'] = input_data
        if ret:
            flushContractToDB(dict_data)
            json_data = json.dumps(dict_data)
            vns_kafka.pushProducer(producer_url, producer_topic, json_data.encode())
            
    else:
        nonce = json_msg['nonce']
        contract_address = vns_web3parse.getContractAddress(address_from, nonce)
        dict_data['contract'] = contract_address
        dict_data['action'] = 'create'
        dict_data['type'] = '0'
        ret = vns_web3parse.parseContract(input_data, vns_bancor_rule, dict_data)
        if ret: 
            print(address_from)
            print(dict_data['name'])
            flushContractToDB(dict_data,True)
            json_data = json.dumps(dict_data)
            vns_kafka.pushProducer(producer_url, producer_topic, json_data.encode())
    
    #flushContractToDB(dict_data)

       
def callbackConsumer(msg):
    print('\n')
    if msg:
        #print(msg)
        if msg.offset % 100 == 0:
            updateOffset(msg.offset)
        print('\n')
        json_value = json.loads(msg.value)
        processMsg(msg.value)



def consumerLoop(offset):
    consumer_url = params['consumerurl']
    consumer_topic = params['consumertopic']
    vns_kafka.syncConsumer(consumer_url, offset, consumer_topic, callbackConsumer)


def main():
    sql = "SELECT `offset` FROM kafka_offset WHERE `name` = '%s' order by id desc  limit 1;" % (params['consumertopic'])
    offset_result = execSql(sql)
    offset_contract = offset_result[0][0]

    sql = 'select contractname, contractbytecode, matchrule from  protocol_vns_bancor where protoid = 1;'
    global vns_bancor_rule 
    vns_bancor_rule = execSql(sql)

    global vns_web3_fn
    sql = "select `fnname`, `fnweb3` from  fnweb3 ;"
    vns_web3_fn = execSql(sql)

    #vns_codeabi.getBancorConverter('0xcfc73f6999527b226ea224d85fb404d568fa2677')
    #vns_codeabi.getVnserToken("0xcfc73f6999527b226ea224d85fb404d568fa2677")
    #vns_codeabi.getSmartToken("0xcfc73f6999527b226ea224d85fb404d568fa2677")
    consumerLoop(offset_contract)
    
    sql = "select input from content where content.`action` = 'undefined';"
    row_input = execSql(sql)
    dict_data = {} 
    for row in row_input:
        vns_web3parse.parseBancorAction(row[0], vns_web3_fn, dict_data)
        print(dict_data)
    
if __name__ == '__main__':
    main()
