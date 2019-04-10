import json
import logging

def readParams(configuer_file):
    json_file = open(configuer_file, 'r') 
    result = json.load(json_file)
    json_file.close()
    print(result) 
    return result

def initLogger(logfilename):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    filter_handler = logging.FileHandler(logfilename, mode = 'w')
    filter_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    filter_handler.setFormatter(formatter)
    logger.addHandler(filter_handler)
    return logger;


