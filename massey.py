import json
import numpy as np
import pprint as pp

def open_file(filename):
	#continually check for correct file input format
	#while !filename.endswith(.json):
	#	print('Incorrect filetype')
	#	print ('Enter new filename: ')
	#	filename = raw_input()
	with open(filename) as data_file:
    	data = json.load(data_file)
    	#genious idea from ben adams to create tuple of array of dicts
    	#from json file, and count of teams
    	return (data, len(set(entry['home']['team'] for i in data)))

def separate(data, team_number):
	teams = {}
	count = 0
	m = []
	y = []
	for i in data:
    	if data['home']['team'] not in teams.keys():
        	data[i['home']['team']] = count
        	count += 1
    	if data['away']['team'] not in teams.keys():
        	data[i['away']['team']] = count
        	count += 1
    	y.append(data['home']['pts'] - data['away']['pts'])
    	m.append([0 for i in range(team_number)])
    	m[-1][teams[i['home']['team']]] = 1
    	m[-1][teams[i['away']['team']]] = -1

    m.append(1 for i in range(team_number))
	y.append(0)

	return (np.array(m), np.array(y), teams)

def team_ranks(rank, teams):
	names = [""] * len(rank)
	for i in teams.keys():
		names[teams[i]] = i
	first50 = zip(names, rank)
	first50 = sorted(first50, key = lambda x: x[-1])
	winners = 50
	for i in range(0, winners):
		print (str(i) + '. ' + str(first50[0]) + ' ' + str(first50[1]) + '\n')

team_number = 0
massey = []
massey, team_number = open_file(sys.argv[1])
m,y,teams = separate(massey, team_number)
r = np.linalg.lstsq(m, y)[0]
team_ranks(r, teams)