from manualWater import readConfig

state = readConfig()
listy = []

for k, v in state.items(): 
	if k == 'manual_mode': 
		print(v)