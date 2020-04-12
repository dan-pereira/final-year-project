import json
import numpy as np
#https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/ to save array

path=''

#TODO

LEARNING_RATE = 0.1 #0-1 high is future low is current
DISCOUNT = 0.95

'''
epsilon must be decayed to learn
1 is exploration 0 is exploitation
'''
epsilon = 0.8

'''
max val = 0.85
min val = 0.25
diff = 0.6
distance away from goal can be +-0.6
'''

envMax = np.array([100]) #sensor max val
envMin = np.array([00]) #sensor min val
granularity = [40] * len(envMax)
tableStates = (envMax - envMin)/granularity

actions = [0.2,0.25,0.3,0.35,0.4,0.45,0.5] 

def crate_q_table():
    q_table = np.random.uniform(low=-2, high=0, size=(granularity + [len(actions)]))
    return

def get_discrete_state(state):
    ''' helper function to get discrete values '''
    discrete_state = (state - envMin)/tableStates
    return tuple(discrete_state.astype(np.int))

def getCurrentState():
    #todo
    states = []
    '''
    return list of 3 discrete_state values
    '''
    get last 3 values from the db for each
    mcp00 = [x,y,z]
    mcp01 = [x,y,z]
    mcp02 = [x,y,z]

    states = [mcp00,mcp01,mcp02]
    return states

def getReward(state,lastState):
    lastDistance = abs(goal-lastState)
    distance = abs(goal-state)
    reward = lastDistance - distance
    return reward

def calculate(q_table, i, config,currentState):
    
    sensor = 'mcp0'+str(i)
    lastState = config['last_state'][sensor]
    goal = config['goal'][sensor]
    actionTaken = config['controller'][i]
    
    reward = getReward(currentState,lastState)
    
    lastQ = q_table[lastState + (actionTaken,)]
    maxQ = np.max(q_table[currentState])

    # Update Q table with Q-value for last action
    improvedQ = (1 - LEARNING_RATE) * lastQ + LEARNING_RATE * (reward + DISCOUNT * maxQ)
    q_table[lastState + (actionTaken,)] = improvedQ
    
    if np.random() > epsilon:
        # Maximum possible Q value for next step & next action
        action = np.argmax(q_table[currentState]) #choose highest ranked action from table
    else:
        action = np.random.randint(0, len(actions)) #pick random action to take
    
    config['controller'][i] = action
    config['last_state'][sensor] = currentState

    return q_table, config


if __name__ == '__main__':


    #openConfig as config

    fileName = path+'q_learn_config.json'
    with open(fileName, 'rvd+') as configFile:
        data=configFile.read()
    config=json.loads(data)

    states = getCurrentState()

    for i in range(3):
        q_table = np.load(path + 'q_table'+str(i))
        q_table, config = calculate(q_table,i,config,states[i])

        np.save(path + 'q_table'+str(i), q_table)

    '''
    rewrite config
    '''
    
    with open(fileName, "r+") as file:
        data = json.load(file)
        data.update(entry)
        json.dump(data, file,indent=2)

if __name__ == '__main__':


    #openConfig as config
    fileName = path+'q_learn_config.json'
    with open(fileName, 'r+') as configFile:
        config=configFile.read()
