import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties # 步驟一
font = FontProperties(fname=r"c:\windows\fonts\msjhl.ttc", size=14) # 步驟二
import os
data = []

esc = int(1)

with open('CBPL_ppit_2020_data.csv', newline='', encoding='utf-8-sig') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
    	if(esc):
    		esc = 0
    	else:
    		if(float(row[2])>=15):
	    		data.append(row)
# 開啟csv檔且將場數高於15場的

for i in range(len(data)):
	for j in range(len(data[0])):
		if (j == 1):
			continue
		else:
			data[i][j] = float(data[i][j])
#把除了名字之外的東西轉成float方便運算

whip = sorted(data , key = lambda s:s[14])
whip_sta = whip[9][14]#以第10名的whip當基準
era = sorted(data , key = lambda s:s[15])
era_sta = era[9][15]#以第10名的era當基準
good = []
for i in range(len(data)):
	if(data[i][14] <= whip_sta and data[i][15] <= era_sta):
		good.append(data[i])
for i in range (len(good)):
	print(good[i])

plt.plot([1,2,3,'早'])
plt.savefig('test.png')
plt.show()

input()
