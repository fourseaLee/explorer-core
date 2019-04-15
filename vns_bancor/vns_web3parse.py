import time 
import vns_web3
import json
from vns_web3 import Web3, HTTPProvider
import rlp

def parseBancorInit(input_data, matchrule, dict_data):
    ret = False
    for row in matchrule:
        code_size = len(row[1])

        if len(input_data) < code_size:
            continue

        if row[2] == 'prefix':
            compare_data = input_data[:code_size]

            if compare_data == row[1]:
                ret = True
                dict_data['name'] = row[0]
                break

        elif row[2] == 'all':
            if input_data == row[1]:
                ret = True
                dict_data['name'] = row[0]
                break

    if ret == False:
        print(input_data)
        dict_data['name'] = 'unknown'
 
    return ret


def parseBancorWeb3fn(fn_name,input_data,dict_data):
    left_size = fn_name.find("(")
    right_size = fn_name.find(")")

    fn_params = fn_name[left_size+1:right_size].split(',')
    websh = vns_web3.Web3()
    if len(fn_params) == 1:
        if fn_params[0] == "address":
            dict_data['param1'] = '0x' + input_data[34:74]
        elif fn_params[0] == "uint256":
            dict_data['param'] =[websh.toInt(hexstr=input_data[-64:])]
        else:
            print(fn_params)
    elif len(fn_params) == 2:
        if fn_params[0] == "address" and fn_params[1] == "uint256":
            dict_data['param'] = ['0x' + input_data[34:74], websh.toInt(hexstr=input_data[-64:])]
            #dict_data['param2'] = websh.toInt(hexstr=input_data[-64:])
        else:
            print(fn_params)
    elif len(fn_params) == 3:
        if fn_params[0] == "address" and fn_params[1] == "uint32" and fn_params[2] == "bool":
            params = True
            if websh.toInt(hexstr=input_data[-64:]):
                params = False
            dict_data['param'] = ['0x'+input_data[34:74], websh.toInt(hexstr = input_data[74:138]),params]
    elif len(fn_params) == 4:
        if fn_params[0] == "address" and fn_params[1] == "address" and fn_params[2] == "uint256" and fn_params[3] == "uint256":
            dict_data['param'] = ['0x'+input_data[34:74], '0x'+input_data[98:138],websh.toInt(hexstr=input_data[138:202]),websh.toInt(hexstr=input_data[202:266])]

def parseBancorAction(input_data, matchrule, dict_data):
    ret = False
    web3_shafn = input_data[:10]
  
    fn_name = ""
    for row in matchrule:
        if row[1] == web3_shafn:
            ret = True
            dict_data['function'] = row[0]
            fn_name = row[0]
            break;
    if ret:
        parseBancorWeb3fn(fn_name,input_data,dict_data)
    else:
        print(input_data)
    return ret
    

def parseContract(input_data, matchrule, dict_data):
    ret = False
    if dict_data['action'] == 'create':
        ret = parseBancorInit(input_data, matchrule, dict_data)
    else:
        ret = parseBancorAction(input_data, matchrule, dict_data)

    return ret




def getTransactionInput(txid):
    transaction = websh.getTransaction(txid)
    if transaction:
        input_data = getTransaction.input
        return input_data
    return input_data
   

def checkIsErc20(tx_input):
    input_prefix = tx_input[:12]
    
    if(input_prefix == '0x60a0604052'):
        return True

    if(input_prefix == '0x6060604052'):
        return True

    if(input_prefix == '0x6080604052'):
        return True

    print(input_prefix)
    return False



def getContractAddress(from_address, nonce):
    encode_address = int(from_address,16)
    encode_nonce = int(nonce,16)
    rlpcode = rlp.encode([encode_address, encode_nonce])
    websh = vns_web3.Web3()
    contract_org = websh.sha3(rlpcode)
    contract_result = '0x' +contract_org.hex()[26:]
    return contract_result



def transferErc20(tx_input):
    results = {}
    websh = vns_web3.Web3()
    address_to  = '0x' + tx_input[34:74]
    balance  = tx_input[-64:]
    balance_value  = websh.toInt(hexstr=balance)
    results['to'] = address_to
    results['total'] = balance_value
    results['tokenAction'] = 'transfer'
    results['tokenStandard'] = 'VRC20'
    results['asset'] = 'VNS'
    return results



def parseInputAction(tx_input):
    results = {}
    except_results = {}
    try:
        contract_action = tx_input[:10]
        if ( contract_action == '0xa9059cbb' ):
            results = transferErc20(tx_input)
        else:
            print(contact_action)
        return results
    except:
        #print(tx_input)
        print('error action\n')
        print(tx_input)
        return except_results


def parseInputCreate(tx_input):
    results = {}
    except_results = {}
    try:
        if(checkIsErc20(tx_input)): 
            input_data = tx_input[-512:]
            websh = vns_web3.Web3()

            total = input_data[:64]
            total_value = websh.toInt(hexstr=total)

            results['total'] = str(total_value)
        
            offset_name = input_data[64:128]
            offset_name_value = websh.toInt(hexstr=offset_name)

            decimal = input_data[128:192]
            decimal_value= websh.toInt(hexstr=decimal)
            results['decimal'] = decimal_value

            offset_symbol = input_data[192:256]
            offset_symbol_value = websh.toInt(hexstr=offset_symbol)
    
            name_size = input_data[256:320]
            name_size_value = websh.toInt(hexstr=name_size)

            name = input_data[320:320 + name_size_value*2]
            name_value = websh.toText(hexstr=name)
            results['name'] = name_value

            symbol_size = input_data[384:448]
            symbol_size_value = websh.toInt(hexstr=symbol_size)

            symbol = input_data[448:448 + symbol_size_value*2]
            symbol_value = websh.toText(hexstr=symbol)
            results['symbol'] = symbol_value
            return results 
    except:
        print(tx_input)
        return except_results






