#Future
#!/usr/bin/python3
import json
import requests
import time
import numpy as np
from database_query import queryDB

sampleQuery = [(82.4743, 61.9565, 79.3804, 23.0, 51.0), (82.9629, 61.7937, 81.1716, 23.0, 50.0),
               (83.1257, 66.516, 79.3804, 23.0, 51.0), (84.4284, 62.1194, 79.2176, 23.0, 51.0),
               (82.1487, 61.9565, 79.7061, 23.0, 50.0)]
path = '/home/ubuntu/src/storage/'
queryString = 'SELECT moisture1,moisture2, moisture3, air_temp,air_humid FROM mydb.sensor_val order by timer desc limit '

LEARNING_RATE = 0.1  # 0-1 high is future low is current
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

# 3 moisture, air temp, air humidity
envMax = np.full((5, 1), 100)  # sensor max val
envMin = np.full((5, 1), 0)  # sensor min val
granularity = [40] * len(envMax)
tableStates = (envMax - envMin) / granularity

possibleActions = [0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]


def crate_q_table():
    q_table = np.random.uniform(low=float(-2), high=float(0), size=(granularity + [len(possibleActions)]))  # initialize with negative rewards
    np.save(path + 'q_table_full', q_table)
    return


def getDiscreteState(value):
    """ helper function to get discrete values """
    # value = [83.028, 62.86842, 79.77122, 23.0, 50.6]
    discrete_state = (value - envMin) / tableStates
    # print(discrete_state.astype(np.int)) #[[33 25 31  9 20][33 25 31  9 20][33 25 31  9 20][33 25 31  9 20][33 25 31  9 20]]
    # print(tuple(discrete_state.astype(np.int))) # (array([33, 25, 31,  9, 20]), array([33, 25, 31,  9, 20]), array([33, 25, 31,  9, 20]), array([33, 25, 31,  9, 20]), array([33, 25, 31,  9, 20]))
    return (discrete_state.astype(np.int))
    # return tuple(discrete_state.astype(np.int))


def reverseDiscrete(states):
    # print(states)
    nonDiscrete = states * tableStates[0]
    result = [nonDiscrete[i][0][0] for i in range(len(nonDiscrete))]
    return result


def getActionStates():
    l = len(possibleActions)
    actions = []
    for a in range(l):
        for b in range(l):
            for c in range(l):
                actions.append([possibleActions[a],possibleActions[b],possibleActions[c]])
    return actions


def getCurrentValues():
    smoothing = 5  # how many states to avg
    # allStates = queryDB(querySring+str(smoothing))
    allStates = sampleQuery
    results = []
    # print(allStates)
    for i in range(len(envMax)):
        # print(i)
        values = []
        for j in range(smoothing):
            # print(' ',j)
            values.append(allStates[j][i])
        results.append(getDiscreteState(np.average(values)))
    return results


def getSensorReward(state, lastState, goal):
    goal = getDiscreteState(goal)[0][0]
    # print('theThree', state, lastState, goal)
    lastDistance = abs(goal - lastState)
    distance = abs(goal - state)
    reward = lastDistance - distance
    print(reward)
    return reward


def getReward(config, currentState, lastState):
    reward = 0
    for i in range(len(config['controller'])):
        currentValue = currentState[i][0][0]
        lastValue = lastState[0][i]
        print('sensor',i)
        reward += getSensorReward(currentValue, lastValue, config['goals'][i])
        # print(currentValue,lastValue,config['goals'][i])
    return reward


def calculate(q_table, config, currentState, actions):
    lastState = config['last_state']

    print('State Change', lastState, '->', reverseDiscrete(currentState))
    lastState = getDiscreteState(lastState)

    # todo actions are incorrect size and range
    # To fix this q_learning model will need to have every state of values and will be 68.9 time bigger
    # todo build q_table on the fly because of so many states that will never be reached

    reward = getReward(config, currentState, lastState)
    print('reward =', reward)

    actionsTaken = config['controller'] #actual Values
    actionTaken = actions.index( actionsTaken) #index of values

    print('actionsTaken', str(actionsTaken))
    print('indexTaken', str(actionTaken))

    lastQ = q_table[lastState][actionTaken]
    print('last->', lastQ)
    maxQ = np.max(q_table[currentState])
    # print('max->', maxQ)

    # Update Q table with Q-value for last action
    improvedQ = (1 - LEARNING_RATE) * lastQ + LEARNING_RATE * (reward + DISCOUNT * maxQ)
    # print('improvedLast->',improvedQ)
    q_table[lastState][actionTaken] = improvedQ

    if np.random.rand() > epsilon:
        # Maximum possible Q value for next step & next action
        actions = np.argmax(q_table[currentState])  # choose highest ranked action from table
        print('+', actions)
    else:
        actions = np.random.randint(0, len(actions))  # pick random action to take
        print('-', actions)

    currentState = reverseDiscrete(currentState)

    print('currState',currentState)
    print('actionsToTake',actions[actions])
    # print(type(actions[action]))

    # print('State Change', reverseDiscrete(lastState), '->', reverseDiscrete(currentState))
    # print(config['goals'])
    # print('actionsTaken', str(actionsTaken))
    # print('reward =', reward)

    #Apply predicted actions
    if config['manual_mode'] == 0:
        config['controller'] = [actions]

    config['last_state'] = currentState

    return q_table, config


if __name__ == '__main__':
    # todo testing area

    # config = {'controller': [0.3, 0.2, 0.3], 'last_state': [82.5, 62.5, 77.5, 22.5, 50.0], 'goals': [71, 73, 75],"manual_mode":0}

    # values = getCurrentValues()
    # print(values)

    # tstCalculate(config, values, possibleActions)
    # q_table, config = calculate(config, values)

    # newV = reverseDiscrete(values)

    # todo testing area

    # fileName = path+'q_learn_config.json'
    # get config
    fileName = path + 'fullDefaultConfig.json'
    with open(fileName, 'r') as configFile:
        data = configFile.read()
    config = json.loads(data)

    config = {'controller': [0.3, 0.2, 0.3], 'last_state': [82.5, 62.5, 77.5, 22.5, 50.0], 'goals': [71, 73, 75], "manual_mode": 1}

    values = getCurrentValues()
    print(values)
    actionStates = getActionStates()

    s = time.time()
    q_table = np.load(path + 'q_table_full.npy')
    e = time.time()
    print(e-s)
    # print('size->',q_table.size)
    # q_table = {}
    q_table, config = calculate(q_table, config, values, actionStates)

    s = time.time()
    np.save(path + 'q_table_full.npy', q_table)
    e = time.time()
    print(e-s)

    print(config)
    # for it in config:
    #    print(it)
    #    print(config[it])

    # write config
    with open(fileName, 'w') as configFile:
        json.dump(config, configFile, indent=2)
    # response = requests.post('http://localhost:5000/update_config', files={'file': open(fileName, 'rb')})
    # print(response)
