
import csv

input_file = csv.DictReader(open("./static/hd2017.csv"))
schools = []
states = []
##Make list of states:
for row in input_file:
    if row['STABBR'] not in states:
        states.append(row['STABBR'])
##Sort Schools VIA State (bc some have name overlaps maybe!)

for row in input_file:
    schools.append(row)

print(states)
#print(schools)
