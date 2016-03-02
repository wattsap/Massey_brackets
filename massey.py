import json
import numpy as pp
import pprint as pp
with open('20152.json') as data_file:
    data = json.load(data_file)

teams = {}
count = 0
m = []
y = []
for i in data:
    if data['home']['team'] not in teams:
        data['home']['team'] = count
        count += 1
    if data['away']['team'] not in teams:
        data['away']['team'] = count
        count += 1
    y.append(data['home']['pts'] - data['away']['pts'])
y.append(0)