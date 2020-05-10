import json
import requests

path = '../storage/'
actualActions = [0.15,0.2,0.25,0.3,0.35,0.4,0.45]
def waterPlant(plantNumber):
    '''
    will hit endpoint on raspi to water
    '''
    plantNo = {'plantNo' : plantNumber}
    response = requests.post('http://localhost:5000/water_plant',data = plantNo)
    print(response.content)
    print('-------plant watered!!---------')
    return('hit')

def readConfig():
    fileName = path+'defaultConfig.json'#'q_learn_config.json'
    with open(fileName, 'r') as configFile:
        data=configFile.read()
    config=json.loads(data)
    return config

def writeConfig(data):
    fileName = path+'defaultConfig.json'#'q_learn_config.json'
    with open(fileName, 'w') as configFile:
        json.dump(data, configFile, indent=2)
    response = requests.post('http://localhost:5000/update_config', files={'file': open(fileName, 'rb')})
    print(response)
    return

def manAutoSelect(val):
    config = readConfig()
    if int(val) == 1:
        config["manual_mode"]=1
        # 1 = manual, 0 = automatic
    else:
        config["manual_mode"]=0
    writeConfig(config)
    return

def updateManValues(plantNo, val):
    actions = [4,5,6,7,8,9,10] #seconds per day
    if val not in actions:
        return "error invalid value"
    val = actions.index(val)
    val = actualActions[val]
    config = readConfig()
    config["manual_mode"]=1
    if str(plantNo) not in config["controller"]:
        return "error invalid value"
    config["controller"][str(plantNo)] = val
    writeConfig(config)
    return

def setGoals(plantNo, val):
    if val not in range(-1,100):
        return "error invalid value"
    config = readConfig()
    if str(plantNo) not in config["goal"]:
        return "error invalid value"
    config["goal"][str(plantNo)] = val
    writeConfig(config)
    return

if __name__ == '__main__':
    print('try')
    #waterPlant()
    manAutoSelect(0)
    print('after')
