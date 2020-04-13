import json
import numpy as np

path='/home/ubuntu/src/storage/'

enm=np.array([100])
enn=np.array([00])
granularity = [40] * len(enm)

tableStates = (enm - enn)/ granularity

def getDiscreteState(state):
    ''' helper function to get discrete values '''
    discrete_state = (state)/tableStates
    return int(discrete_state)

def reverseDiscrete(state):
    result = state * tableStates[0]
    return int(result)

#q_table = np.random.uniform(low=float(-2), high=float(0), size=(granularity + [7]))
#np.save(path + 'sample'+str(0)+'.npy',q_table)

tba = np.load(path + 'q_table0.npy')
tbb = np.load(path + 'q_table0cp.npy')

#print(getDiscreteState(100))

#print(type(tbl[39][0]))
'''
i = 0
while i < len(tba)-1:
    if tba[i].all() == tbb[i].all():
        print('equal')
    else:
        print(tba[i])
    i += 1
'''


fileName = path + 'q_learn_config.json'
with open(fileName, 'r') as configFile:
    data=configFile.read()
config=json.loads(data)

print(config)
'''
actionTaken = config['controller']['1']
print(actionTaken)
state = config['goal']['mcp00']
print(state)
dstate = getDiscreteState(state)
print(dstate)
print(reverseDiscrete(dstate))
'''
