import json
import sys
import numpy as np
import pprint as pp

def open_file(filename):
	with open(filename) as data_file:
		json_stats = json.load(data_file)
		#genious idea from ben adams to create tuple of array of dicts
		#from json file, and count of teams
		return (json_stats, len(set([i['home']['team'] for i in json_stats])))

def separate(json_stats, team_number):
	teams = {}
	count = 0
	m = []
	y = []
	advantage = 3
	home_team = 1
	away_team = -1
	count_add = 1
	m_score_mod = 1
	y_score_mod = 0
	m_filler = 0
	end_list = -1
	team_len = len(teams)
	for i in json_stats:
		'''
		if i['home']['team'] not in teams:
			teams[i['home']['team']] = count
			count += count_add
		if i['away']['team'] not in teams:
			teams[i['away']['team']] = count
			count += count_add
		'''
		#theoretically does the same thing as the 2 if statements above
		teams.setdefault(i['home']['team'], team_len)
		teams.setdefault(i['away']['team'], team_len)
		row = [0] * team_len
		'''
		y.append(i['home']['pts'] - i['away']['pts'] - advantage)
		m.append([m_filler for x in range(team_number)])
		m[end_list][teams[i['home']['team']]] = home_team
		m[end_list][teams[i['away']['team']]] = away_team
	m.append(m_score_mod for i in range(team_number))
	y.append(y_score_mod)
	   '''
		row[teams[i['home']['team']]] = 1
		row[teams[i['away']['team']]] = -1
		m.append(row)
		y.append(g['home']['pts'] - g['away']['pts'])
	m.append(1 * team_len)
	y.append(0)
	return (np.array(m), np.array(y), teams)

def team_ranks(rank, teams):
	winner_display_number = 50
	round_rank = 2
	end_list = -1
	populate = None
	fix_inc_print = 1
	access_2nd_tuple_zero = 0
	access_2nd_tuple_one = 1
	names = [populate] * len(rank)
	for i in teams.keys():
		names[teams[i]] = i
	first_50 = zip(names, rank)
	first_50 = list(reversed(sorted(first_50, key = lambda x: x[end_list])))
	for i in range(winner_display_number):
		print (str(i+fix_inc_print) + '. ' + str(first_50[i][access_2nd_tuple_zero]) 
			+ ' ' + str(round(first_50[i][access_2nd_tuple_one], round_rank)) + '\n')

team_number = 0
massey = []
arg_length = 2
second_arg = 1
access_2nd_tuple_zero = 0
if len(sys.argv) != arg_length:
	massey, team_number = open_file(input('Enter filename:\t'))
else:
	massey, team_number = open_file(sys.argv[second_arg])
m,y,teams = separate(massey, team_number)
r = np.linalg.lstsq(m, y)[access_2nd_tuple_zero]
team_ranks(r, teams)