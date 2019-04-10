import json
import vns_web3
from vns_web3 import Web3, HTTPProvider
import rlp
from solc import compile_source
from web3.contract import ConciseContract
web3 = Web3(HTTPProvider('http://120.27.232.146:8585'))
web3.vns.defaultAccount = '0xa9632c83a3f53f6ffa800f5d7b6410f7f481fa9a'

def getBancorConverter():
    json_file = open('code/BancorConverter.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorConverter.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()
    
    bancor_converter = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_converter
    
def getBancorConverterFactory():
    json_file = open('code/BancorConverterFactory.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorConverterFactory.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_converter_factory = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_converter_factory
    

def getBancorConverterUpgrader():
    json_file = open('code/BancorConverterUpgrader.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorConverterUpgrader.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_converter_upgrader = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_converter_upgrader
    
def getBancorFormula():
    json_file = open('code/BancorFormula.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorFormula.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_formula = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_formula
    
def getBancorGasPriceLimit():
    json_file = open('code/BancorGasPriceLimit.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorGasPriceLimit.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_gas_price_limit = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_gas_price_limit
    
def getBancorNetWork():
    json_file = open('code/BancorNetwork.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorNetwork.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_network = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_network
    

def getBancorPriceFloor():
    json_file = open('code/BancorPriceFloor.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorPriceFloor.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_price_floor = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_price_floor
    
def getBancorX():
    json_file = open('code/BancorX.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/BancorX.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    bancor_x = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_x
    

def getContractFeatures():
    json_file = open('code/ContractFeatures.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ContractFeatures.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    contract_features = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return contract_features
    
def getContractIds():
    json_file = open('code/ContractIds.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ContractIds.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    contract_ids = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return contract_ids
    

def getContractRegistry():
    json_file = open('code/ContractRegistry.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ContractRegistry.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    contract_registry = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return contract_registry
    
def getCrowdsaleController():
    json_file = open('code/CrowdsaleController.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/CrowdsaleController.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    crow_sale_controller = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return crow_sale_controller
    
def getERC20Token():
    json_file = open('code/ERC20Token.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ERC20Token.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    erc20_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return erc20_token
    
def getEtherToken():
    json_file = open('code/EtherToken.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    print(json_abi)

    bin_file = open('code/EtherToken.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ether_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ether_token
    

def getFeatureIds():
    json_file = open('code/FeatureIds.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/FeatureIds.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    feature_ids = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return feature_ids
    
def getIBancorConverter():
    json_file = open('code/IBancorConverter.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorConverter.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_converter = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancor_converter
    

def getIBancorConverterExtended():
    json_file = open('code/IBancorConverterExtended.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorConverterExtended.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_converter_extended = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancor_converter_extended
    
def getIBancorConverterFactory():
    json_file = open('code/IBancorConverterFactory.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorConverterFactory.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_converter_factory = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_converter_factory
    

def getIBancorConverterUpgrader():
    json_file = open('code/IBancorConverterUpgrader.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorConverterUpgrader.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_converter_upgrader = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return  ibancor_converter_upgrader
    
def getIBancorFormula():
    json_file = open('code/IBancorFormula.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorFormula.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_formula = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancor_formula
    
def getIBancorGasPriceLimit():
    json_file = open('code/IBancorGasPriceLimit.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorGasPriceLimit.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_gas_price_limit = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancor_gas_price_limit

    
def getIBancorNetwork():
    json_file = open('code/IBancorNetwork.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorNetwork.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_network = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancor_network
    

def getIBancorX():
    json_file = open('code/IBancorX.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorX.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancor_x = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return bancor_x
    
def getIBancorXUpgrader():
    json_file = open('code/IBancorXUpgrader.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IBancorXUpgrader.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ibancorx_upgrader = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ibancorx_upgrader
    

def getIContractFeatures():
    json_file = open('code/IContractFeatures.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IContractFeatures.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    icontract_features = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return icontract_features
    
def getIContractRegistry():
    json_file = open('code/IContractRegistry.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IContractRegistry.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    icontract_registry = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return icontract_registry
    

def getIERC20Token():
    json_file = open('code/IERC20Token.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IERC20Token.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ierc20_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ierc20_token
    
def getIEtherToken():
    json_file = open('code/IEtherToken.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IEtherToken.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    iether_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return iether_token
    
def getINonStandardERC20():
    json_file = open('code/INonStandardERC20.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/INonStandardERC20.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    inonstandard_erc20 = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return inonstandard_erc20
    
def getIOwned():
    json_file = open('code/IOwned.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IOwned.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    iowned = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return iowned
    

def getISmartToken():
    json_file = open('code/ISmartToken.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ISmartToken.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    ismart_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return ismart_token
    
def getITokenHolder():
    json_file = open('code/ITokenHolder.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ITokenHolder.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    itoken_holder = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return itoken_holder
    

def getITokenHolder():
    json_file = open('code/ITokenHolder.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/ITokenHolder.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    itoken_holder = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return itoken_holder
    
def getIWhitelist():
    json_file = open('code/IWhitelist.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/IWhitelist.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    iwhitelist = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return iwhitelist
    

def getManaged():
    json_file = open('code/Managed.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/Managed.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    managed = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return managed
    
def getMigrations():
    json_file = open('code/Migrations.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/Migrations.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    migrations = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return migrations
    
def getNonStandardTokenRegistry():
    json_file = open('code/NonStandardTokenRegistry.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/NonStandardTokenRegistry.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    non_standard_token_registry = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return non_standard_token_registry
    
def getOwned():
    json_file = open('code/Owned.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/Owned.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    owned = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return owned
    

def getSafeMath():
    json_file = open('code/SafeMath.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/SafeMath.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    safe_math = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return safe_math
    
def getSmartToken():
    json_file = open('code/SmartToken.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/SmartToken.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    smart_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return smart_token
    

def getSmartTokenController():
    json_file = open('code/SmartTokenController.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/SmartTokenController.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    smart_token_controller = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return smart_token_controller
    
def getTestBancorFormula():
    json_file = open('code/TestBancorFormula.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/TestBancorFormula.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    test_bancor_formula = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return test_bancor_formula
    

def getTestCrowdsaleController():
    json_file = open('code/TestCrowdsaleController.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/TestCrowdsaleController.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    test_crowdsale_controller = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return test_crowdsale_controller
    
def getTestERC20Token():
    json_file = open('code/TestERC20Token.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/TestERC20Token.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    test_erc20_token = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return test_erc20_token
    
def getTestFeatures():
    json_file = open('code/TestFeatures.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/TestFeatures.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    test_features = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return test_features
    
def getTestUtils():
    json_file = open('code/TestUtils.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/TestUtils.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    test_utils = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return test_utils
    

def getUtils():
    json_file = open('code/Utils.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/Utils.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    utils = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return utils
    
def getWhitelist():
    json_file = open('code/Whitelist.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/Whitelist.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    white_list = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return white_list
    

def getXTransferRerouter():
    json_file = open('code/XTransferRerouter.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('code/XTransferRerouter.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    xtransfer_rerouter = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return xtransfer_rerouter
    
     
