from bs4 import BeautifulSoup

import requests

import re
import csv

team = "gonzaga"
r = requests.get("http://sports-reference.com/cbb/schools/" + team + "/2018.html")

data = r.text

soup = BeautifulSoup(data, "html.parser")

page = soup.getText()
# print(page)

table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "team_stats")
rows = table.findAll(lambda tag: tag.name == 'tr')
num = len(rows) - 4
statrow = rows[num]

#print(statrow)
statrow = str(statrow).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
print(statrow)
line = re.findall('Overall.+', page)[0]
rec = re.findall('[\d]+\-[\d]+', line)[0]
wl = re.findall('[\d]+', rec)
win = wl[0]
lose = wl[1]

line2 = re.findall('PS/G.+', page)[0]
pointsScored = re.findall('[\d]+\.[\d]', line2)[0]
line3 = re.findall('PA/G.+', page)[0]
pointsAllowed = re.findall('[\d]+\.[\d]', line3)[0]

teamstatsline = re.findall('Team[\d\.]+', page)[0]
percents = re.findall('\.\d\d\d', teamstatsline)
fg = re.findall('fg">[\d]+<', statrow)[0]
fg=re.findall('[\d]+',fg)[0]
print(fg)
fga = re.findall('fga">[\d]+<', statrow)[0]
fga=re.findall('[\d]+',fga)[0]
print(fga)
twop = re.findall('fg2">[\d]+<', statrow)[0]
twop=re.findall('[\d][\d]+',twop)[0]
print(twop)

print(percents)

# Print Page
print(line)
print(rec)
print(win)
print(lose)
print(pointsScored)
print(pointsAllowed)
