import json
import vns_web3
from vns_web3 import Web3, HTTPProvider
import rlp
from solc import compile_source
from web3.contract import ConciseContract
web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def getBancorConverter(contract_address):
    json_file = open('vns_code/BancorConverter.json', 'r')
    json_data = json.load(json_file)
    json_abi = json_data['abi']
    json_file.close()
    
    bancor_converter = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_converter


def getBancorConverterFactory(contract_address):
    json_file = open('vns_code/BancorConverterFactory.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_converter_factory = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_converter_factory
    

def getBancorConverterUpgrader(contract_address):
    json_file = open('vns_code/BancorConverterUpgrader.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_converter_upgrader = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_converter_upgrader


def getBancorFormula(contract_address):
    json_file = open('vns_code/BancorFormula.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_formula = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_formula


def getBancorGasPriceLimit(contract_address):
    json_file = open('vns_code/BancorGasPriceLimit.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_gas_price_limit = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_gas_price_limit


def getBancorNetWork(contract_address):
    json_file = open('vns_code/BancorNetwork.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_network = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_network
    

def getBancorPriceFloor(contract_address):
    json_file = open('vns_code/BancorPriceFloor.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_price_floor = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_price_floor


def getBancorX(contract_address):
    json_file = open('vns_code/BancorX.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    bancor_x = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_x
    

def getContractFeatures(contract_address):
    json_file = open('vns_code/ContractFeatures.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    contract_features = web3.vns.contract(address=contract_address, abi=json_abi)
    return contract_features


def getContractIds(contract_address):
    json_file = open('vns_code/ContractIds.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    contract_ids = web3.vns.contract(address=contract_address, abi=json_abi)
    return contract_ids
    

def getContractRegistry(contract_address):
    json_file = open('vns_code/ContractRegistry.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    contract_registry = web3.vns.contract(address=contract_address, abi=json_abi)
    return contract_registry


def getCrowdsaleController(contract_address):
    json_file = open('vns_code/CrowdsaleController.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    crow_sale_controller = web3.vns.contract(address=contract_address, abi=json_abi)
    return crow_sale_controller


def getERC20Token(contract_address):
    json_file = open('vns_code/ERC20Token.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    erc20_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return erc20_token


def getEtherToken(contract_address):
    json_file = open('vns_code/EtherToken.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    print(json_abi)

    json_abi = json_data['abi']
    ether_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return ether_token
    

def getFeatureIds(contract_address):
    json_file = open('vns_code/FeatureIds.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    feature_ids = web3.vns.contract(address=contract_address, abi=json_abi)
    return feature_ids


def getIBancorConverter(contract_address):
    json_file = open('vns_code/IBancorConverter.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_converter = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancor_converter
    

def getIBancorConverterExtended(contract_address):
    json_file = open('vns_code/IBancorConverterExtended.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_converter_extended = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancor_converter_extended


def getIBancorConverterFactory(contract_address):
    json_file = open('vns_code/IBancorConverterFactory.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_converter_factory = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_converter_factory
    

def getIBancorConverterUpgrader(contract_address):
    json_file = open('vns_code/IBancorConverterUpgrader.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_converter_upgrader = web3.vns.contract(address=contract_address, abi=json_abi)
    return  ibancor_converter_upgrader


def getIBancorFormula(contract_address):
    json_file = open('vns_code/IBancorFormula.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_formula = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancor_formula


def getIBancorGasPriceLimit(contract_address):
    json_file = open('vns_code/IBancorGasPriceLimit.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_gas_price_limit = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancor_gas_price_limit

    
def getIBancorNetwork(contract_address):
    json_file = open('vns_code/IBancorNetwork.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_network = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancor_network
    

def getIBancorX(contract_address):
    json_file = open('vns_code/IBancorX.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancor_x = web3.vns.contract(address=contract_address, abi=json_abi)
    return bancor_x


def getIBancorXUpgrader(contract_address):
    json_file = open('vns_code/IBancorXUpgrader.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ibancorx_upgrader = web3.vns.contract(address=contract_address, abi=json_abi)
    return ibancorx_upgrader
    

def getIContractFeatures(contract_address):
    json_file = open('vns_code/IContractFeatures.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    icontract_features = web3.vns.contract(address=contract_address, abi=json_abi)
    return icontract_features


def getIContractRegistry(contract_address):
    json_file = open('vns_code/IContractRegistry.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    icontract_registry = web3.vns.contract(address=contract_address, abi=json_abi)
    return icontract_registry
    

def getIERC20Token(contract_address):
    json_file = open('vns_code/IERC20Token.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ierc20_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return ierc20_token


def getIEtherToken(contract_address):
    json_file = open('vns_code/IEtherToken.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    iether_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return iether_token


def getINonStandardERC20(contract_address):
    json_file = open('vns_code/INonStandardERC20.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    inonstandard_erc20 = web3.vns.contract(address=contract_address, abi=json_abi)
    return inonstandard_erc20


def getIOwned(contract_address):
    json_file = open('vns_code/IOwned.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    iowned = web3.vns.contract(address=contract_address, abi=json_abi)
    return iowned
    

def getISmartToken(contract_address):
    json_file = open('vns_code/ISmartToken.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    ismart_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return ismart_token


def getITokenHolder(contract_address):
    json_file = open('vns_code/ITokenHolder.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    itoken_holder = web3.vns.contract(address=contract_address, abi=json_abi)
    return itoken_holder
    

def getITokenHolder(contract_address):
    json_file = open('vns_code/ITokenHolder.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    itoken_holder = web3.vns.contract(address=contract_address, abi=json_abi)
    return itoken_holder


def getIWhitelist(contract_address):
    json_file = open('vns_code/IWhitelist.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    iwhitelist = web3.vns.contract(address=contract_address, abi=json_abi)
    return iwhitelist
    

def getManaged(contract_address):
    json_file = open('vns_code/Managed.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    managed = web3.vns.contract(address=contract_address, abi=json_abi)
    return managed


def getMigrations(contract_address):
    json_file = open('vns_code/Migrations.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    migrations = web3.vns.contract(address=contract_address, abi=json_abi)
    return migrations


def getNonStandardTokenRegistry(contract_address):
    json_file = open('vns_code/NonStandardTokenRegistry.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    non_standard_token_registry = web3.vns.contract(address=contract_address, abi=json_abi)
    return non_standard_token_registry


def getOwned(contract_address):
    json_file = open('vns_code/Owned.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    owned = web3.vns.contract(address=contract_address, abi=json_abi)
    return owned
    

def getSafeMath(contract_address):
    json_file = open('vns_code/SafeMath.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    safe_math = web3.vns.contract(address=contract_address, abi=json_abi)
    return safe_math


def getSmartToken(contract_address):
    json_file = open('vns_code/SmartToken.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    smart_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return smart_token
    

def getSmartTokenController(contract_address):
    json_file = open('vns_code/SmartTokenController.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    smart_token_controller = web3.vns.contract(address=contract_address, abi=json_abi)
    return smart_token_controller


def getTestBancorFormula(contract_address):
    json_file = open('vns_code/TestBancorFormula.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    test_bancor_formula = web3.vns.contract(address=contract_address, abi=json_abi)
    return test_bancor_formula
    

def getTestCrowdsaleController(contract_address):
    json_file = open('vns_code/TestCrowdsaleController.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    test_crowdsale_controller = web3.vns.contract(address=contract_address, abi=json_abi)
    return test_crowdsale_controller


def getTestERC20Token(contract_address):
    json_file = open('vns_code/TestERC20Token.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    test_erc20_token = web3.vns.contract(address=contract_address, abi=json_abi)
    return test_erc20_token


def getTestFeatures(contract_address):
    json_file = open('vns_code/TestFeatures.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    test_features = web3.vns.contract(address=contract_address, abi=json_abi)
    return test_features


def getTestUtils(contract_address):
    json_file = open('vns_code/TestUtils.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    test_utils = web3.vns.contract(address=contract_address, abi=json_abi)
    return test_utils
    

def getUtils(contract_address):
    json_file = open('vns_code/Utils.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    utils = web3.vns.contract(address=contract_address, abi=json_abi)
    return utils
    

def getWhitelist(contract_address):
    json_file = open('vns_code/Whitelist.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    white_list = web3.vns.contract(address=contract_address, abi=json_abi)
    return white_list
    

def getXTransferRerouter(contract_address):
    json_file = open('vns_code/XTransferRerouter.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    json_abi = json_data['abi']
    xtransfer_rerouter = web3.vns.contract(address=contract_address, abi=json_abi)
    return xtransfer_rerouter
    
     
