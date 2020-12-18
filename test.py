import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd

data = []
datatype = ['NAME','G','PA','AB','RBI','R','H','1B','2B','3B','HR','TB','SO','SB','OBP','SLG','AVG','GIDP','SAC','SF','BB','IBB','HBP','CS','GO','AO','G/F','SB%','TA','SSA']
datatype2 = ['NAME','G','GS','GR','CG','SHO','NBB','W','L','SV','BS','HLD','IP','WHIP','ERA','BF','NP','H','HR','BB','IBB','HBP','SO','WP','BK','R','ER','GO','AO','G/F']
year = int(2019)
page = int(0)

def get_data(year):
	for page in range (10):
		url = 'http://www.cpbl.com.tw/en/stats/all.html?year='+str(year)+'&stat=ppit&online=1&sort=G&order=desc&per_page='+str(page)
		allpage = BeautifulSoup(requests.get(url).text,'html.parser')
		name = allpage.find_all('td',align = 'left')
		dis1 = allpage.find_all('td',re.compile('display1'))
		dis2 = allpage.find_all('td',re.compile('display2'))
		for i in range (len(name)):#看這一頁有幾個人
			score = []
			score.append(name[i].text)
			for j in range (14):
				score.append(dis1[i*14+j].text)
			for j in range (15):
				score.append(dis2[i*15+j].text)
			data.append(score)

get_data(2019)

excel = pd.DataFrame(data)
excel.columns = datatype2
excel.to_csv('CBPL_	'+str(year)+'年資料.csv' , encoding = 'UTF-8-sig')