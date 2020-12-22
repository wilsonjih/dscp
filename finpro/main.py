import csv

data = []

with open('CBPL_ppit_2019_data.csv', newline='', encoding='utf-8-sig') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
    	data.append(row)
print(data)