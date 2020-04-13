import json
import requests
import numpy as np
from database_query import queryDB

path='/home/ubuntu/src/storage/'

LEARNING_RATE = 0.1 #0-1 high is future low is current
DISCOUNT = 0.95

'''
epsilon must be decayed to learn
1 is exploration 0 is exploitation
'''
epsilon = 0.1

'''
max val = 0.85
min val = 0.25
diff = 0.6
distance away from goal can be +-100
'''

envMax = np.array([100]) #sensor max val
envMin = np.array([00]) #sensor min val
granularity = [40] * len(envMax)
tableStates = (envMax - envMin)/granularity

actions = [0.2,0.25,0.3,0.35,0.4,0.45,0.5]

def crate_q_table(i):
    q_table = np.random.uniform(low=float(-2), high=float(0), size=(granularity + [len(actions)]))
    np.save(path + 'q_table'+str(i), q_table)
    return

def getDiscreteState(state):
    ''' helper function to get discrete values '''
    discrete_state = (state - envMin)/tableStates
    return int(discrete_state)

def reverseDiscrete(state):
    result = state * tableStates[0]
    return int(result)

def getCurrentState():
    smoothing = 5 #how many states to avg
    allStates = queryDB('SELECT moisture1,moisture2, moisture3 FROM mydb.sensor_val order by timer desc limit '+str(smoothing))
    results = []
    #print(allStates)
    for i in range(3):
        #print(i)
        states = []
        for j in range(smoothing):
            #print(' ',j)
            states.append(allStates[j][i])
        results.append(getDiscreteState(np.average(states)))
    return results

def getReward(state,lastState,goal):
    lastDistance = abs(goal-lastState)
    distance = abs(goal-state)
    reward = lastDistance - distance
    return reward

def calculate(q_table, i, config,currentState):
    sensor = 'mcp0'+str(i)
    lastState = config['last_state'][sensor]
    lastState = getDiscreteState(lastState)
    goal = config['goal'][sensor]
    goal = getDiscreteState(goal)
    actionTaken = config['controller'][str(i)]
    actionTaken = actions.index(actionTaken)

    reward = getReward(currentState,lastState,goal)

    print('lastState',lastState)
    print('goal', goal)
    print('actionTaken',actionTaken,str(actions[actionTaken])+'s')
    print('reward =', reward)
    lastQ = q_table[lastState][actionTaken]
    maxQ = np.max(q_table[currentState])

    # Update Q table with Q-value for last action
    improvedQ = (1 - LEARNING_RATE) * lastQ + LEARNING_RATE * (reward + DISCOUNT * maxQ)
    q_table[lastState][actionTaken] = improvedQ

    if np.random.rand() > epsilon:
        # Maximum possible Q value for next step & next action
        action = np.argmax(q_table[currentState]) #choose highest ranked action from table
    else:
        action = np.random.randint(0, len(actions)) #pick random action to take

    currentState = reverseDiscrete(currentState)

    #print('action',actions[action])
    #print(type(actions[action]))
    config['controller'][str(i)] = actions[action]
    config['last_state'][sensor] = currentState

    return q_table, config


if __name__ == '__main__':

    fileName = path+'q_learn_config.json'
    #get config
    with open(fileName, 'r') as configFile:
        data=configFile.read()
    config=json.loads(data)
    cfa = config

    states = getCurrentState()

    for i in range(3):
        q_table = np.load(path + 'q_table'+str(i)+'.npy')
        q_table, config = calculate(q_table,i,config,states[i])
        np.save(path + 'q_table'+str(i)+'.npy', q_table)

    #print(config)
    #for it in config:
    #    print(it)
    #    print(config[it])
    #write config

    with open(fileName, 'w') as configFile:
        json.dump(config, configFile, indent=2)
    response = requests.post('http://localhost:5000/update_config', files={'file': open(fileName, 'rb')})
    print(response)
