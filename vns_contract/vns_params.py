import json

def readParams(configuer_file):
    json_file = open(configuer_file, 'r') 
    result = json.load(json_file)
    json_file.close()
    print(result) 
    return result
