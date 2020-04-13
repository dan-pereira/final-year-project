import json
import numpy as np

path = ''

envMax = np.array([100]) #number of state variables = len of array
envMin = np.array([-100])
envMax = np.array([0.6]) #sensor max val
envMin = np.array([-0.6]) #sensor min val
granularity = [40] * len(envMax)
tableStates = (envMax - envMin)/granularity

actions = [0.2,0.25,0.3,0.35,0.4,0.45,0.5]

def create_q_table():
    #init table
    #[24] is the granularity
    granularity = [40] * len(envMax)

    #every combination of states
    tableStates = (envMax - envMin)/granularity

    #init q_table with random vals
    q_table = np.random.uniform(low=-90, high=90, size=(granularity + [len(actions)]))

    return q_table

def saveTable(table):
    np.save('date.npy', table)


def readTable():
    data = np.load('date.npy')
    return data

configFile = 'config.json'
readFile = 'q_learn_config.json'
def createConfig():
    with open(configFile, 'a') as file:
        empty={}
        json.dump(empty, file,indent=2)
    return

def readConfig():
    with open(configFile, 'r') as json_file:
        data = json_file.read()
        json_vals = json.loads(data)
        print(json_vals)
    return json_vals

def rewriteConfig(json_vals):
    with open(configFile, 'w') as cf:
        json.dump(json_vals, cf, indent=2)
    return


def get_discrete_state(state):
    ''' helper function to get discrete values '''
    discrete_state = (state - envMin)/tableStates
    return (discrete_state.astype(np.int))

if __name__ == '__main__':

    #createConfig()

    vals = readConfig()

    vals['controller']['1'] = 315

    rewriteConfig(vals)

    #print(get_discrete_state(14))
    #q_table = create_q_table()

    #print(q_table)

    #print('start')
    #save(q_table)
    #print('end')
    #q_tablen = reada()
    #print(q_tablen)

