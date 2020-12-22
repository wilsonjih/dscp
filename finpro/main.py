import csv


with open('CBPL_ppit_2019_data.csv', newline='', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)