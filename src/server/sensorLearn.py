import numpy as np
#https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/ to save array

#TODO
'''
implement functions
apply discount rate
open close:
    q_table
    pump config
'''

LEARNING_RATE = 0.1 #0-1 high is future low is current
DISCOUNT = 0.95

'''
epsilon must be decayed to learn
1 is exploration 0 is exploitation
'''
epsilon = 1

envMax = np.array([0.85]) #sensor max val
envMin = np.array([0.25]) #sensor min val

actions = [0,1,2] #reduce keep increase
    #define a min to reduce by

#init table
#[20] is the granularity
granularity = [20] * len(envMax)

#every combination of states
tableStates = (envMax - envMin)/granularity

print(tableStates)

#init q_table with random vals
q_table = np.random.uniform(low=-2, high=0, size=(granularity + [len(actions)]))

def getLastState():
    pass

def getCurrentState():
    pass

def getReward():
    pass

def performAction():
    '''
    check for config file
    0,1,2 decrease, no change, increase
    save file and send http to pi flask
    '''
    return

def get_discrete_state(state):
    ''' helper function to get discrete values '''
    discrete_state = (state - envMin)/tableStates
    return tuple(discrete_state.astype(np.int))





#Open table


#0
# Get states
lastState = getLastState()
state = getCurrentState()
#find reward
reward = getReward()

# Get last action & Q-value for last state
lastQ = q_table[lastState + (actionTaken,)]
actionTaken = np.argmax(q_table[lastState])

# Maximum possible Q value for next step & next action
maxQ = np.max(q_table[currentState])
action = np.argmax(q_table[currentState]) #choose highest ranked action from table

# Update Q table with Q-value for last action
improvedQ = (1 - LEARNING_RATE) * lastQ + LEARNING_RATE * (reward + DISCOUNT * maxQ)
q_table[lastState + (actionTaken,)] = improvedQ

#1

performAction(action)

#Save q_table
