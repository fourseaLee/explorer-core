import time 
import vns_web3
import json
from vns_web3 import Web3, HTTPProvider
import rlp
websh = Web3(HTTPProvider('http://192.168.0.40:8585'))


def getTotalAndDecimals(address,dict_data):
    contract_address = websh.toChecksumAddress(address)
    call_total={"data":"0x18160ddd", "to":contract_address}
    data = websh.vns.call(call_total)
    hex_data = websh.toHex(data)
    if hex_data == '0x':
        return False 
    value = websh.toInt(hexstr=hex_data)
    dict_data['total'] = str(value)
    
    call_decimals={"data":"0x313ce567", "to":contract_address}
    data = websh.vns.call(call_decimals)
    hex_data = websh.toHex(data)
    value = websh.toInt(hexstr=hex_data)
    dict_data['decimal'] = value
    return True

def checkIsErc20(tx_input):
    input_prefix = tx_input[:12]
    print("vrc20") 
    if(input_prefix == '0x60a0604052'):
        return True

    if(input_prefix == '0x6060604052'):
        return True

    input_prefix = tx_input[:76]

    if (input_prefix == '0x60806040526002805460ff1916601217905534801561001d57600080fd5b506040516109e1'):
        return True

    return False;

def checkIsBancorVrc20(tx_input,dict_data):
   
    input_prefix46 = tx_input[:46]
    print("bancorvrc20")
    print(input_prefix46)
    if(input_prefix46 == '0x60c0604052600960808190527f546f6b656e20302e31'):
        dict_data["tokenStandard"] = 'BancorVrc10'
        return True
    print(input_prefix46)
  
    input_prefix60 = tx_input[:60]
    if(input_prefix60 == '0x606060405260408051908101604052600981527f546f6b656e20302e31'):
        dict_data["tokenStandard"] = 'BancorVrc20'
        return True

    input_prefix76 = tx_input[:76]
    if(input_prefix76 == '0x60806040526002805460ff1916601217905534801561001d57600080fd5b506040516109c6'):
        dict_data["tokenStandard"] = 'bancorVRC20'
        return True

    input_prefix12 = tx_input[:12]
    if(input_prefix12 == '0x60c0604052'):
        dict_data["tokenStandard"] = 'BancorVrc30'
        return True

    if(input_prefix12 == '0x6080604052'):
        dict_data["tokenStandard"] = 'BancorVrc40'
        return True

    print(input_prefix12)
    return False;



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
    balance  = tx_input[74:]
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
        #print(tx_input)
        return except_results

def checkIs512(tx_input,dict_data):
    input_prefix36 = tx_input[:36]
    if(input_prefix36 == '0x60a0604052600460608190527f48302e31'):
        dict_data['tokenStandard'] = 'VNSCredit'
        return True

    input_prefix50 = tx_input[:50]

    if(input_prefix50 == '0x606060405260408051908101604052600481527f48302e31'):
        dict_data['tokenStandard'] = 'VNSUNKnow'
        return True

    input_prefix48 = tx_input[:48]
    if(input_prefix48 == '0x606060405260408051908101604052600381527f302e39'):
        dict_data['tokenStandard'] = 'VRC20'
        return True

    input_prefix76 = tx_input[:76]
    if (input_prefix76 == '0x60806040526002805460ff1916601217905534801561001d57600080fd5b506040516109e1'):
        dict_data['tokenStandard'] = 'VRC20'
        return True


    return False

def parseInputCreate(tx_input):
    results = {}
    except_results = {}
    try:
        if checkIs512(tx_input,results):
            input_data = tx_input[-512:]
            #print(input_data)
            websh = vns_web3.Web3()

            total = input_data[:64]
            total_value = websh.toInt(hexstr=total)

            results['total'] = str(total_value)
        
            offset_name = input_data[64:128]
            offset_name_value = websh.toInt(hexstr=offset_name)

            decimal = input_data[128:192]
            decimal_value= websh.toInt(hexstr=decimal)
            #results['decimal'] = decimal_value
           
            offset_symbol = input_data[192:256]
            offset_symbol_value = websh.toInt(hexstr=offset_symbol)
            if results['tokenStandard'] == 'VRC20':
                results['decimal'] = offset_symbol_value
            else:
                results['decimal'] = decimal_value


            #print(total)
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
            #results['tokenStandard'] = 'VRC20'
            return results
        elif checkIsBancorVrc20(tx_input,results):
            input_data = tx_input[-448:]
            websh = vns_web3.Web3()
            #print(input_data)
            total = input_data[:64]
            total_value = websh.toInt(hexstr=total)

            results['total'] = str(total_value)
        
            offset_name = input_data[64:128]
            offset_name_value = websh.toInt(hexstr=offset_name)

            decimal = input_data[128:192]
            decimal_value= websh.toInt(hexstr=decimal)
            results['decimal'] = decimal_value

            name_size = input_data[192:256]
            name_size_value = websh.toInt(hexstr=name_size)

            name = input_data[256:256 + name_size_value*2]
            name_value = websh.toText(hexstr=name)
            results['name'] = name_value

            symbol_size = input_data[320:384]
            symbol_size_value = websh.toInt(hexstr=symbol_size)

            symbol = input_data[384:384 + symbol_size_value*2]
            symbol_value = websh.toText(hexstr=symbol)
            results['symbol'] = symbol_value
            #results['tokenStandard'] = 'bancorVRC20'
            return results 

    except:
        print("error create")
        
        return except_results






