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
oppstatrow=rows[num+2]

statrow = str(statrow).replace('tr&gt;', '').replace('th&gt;', '').replace('td&gt;', '').replace('&lt;', '').replace(
    '&gt', '').replace('/', '').replace(';', '').replace('span', '').replace('undermark', '').replace('overermark',
                                                                                                      '').replace(
    'class=', '').replace('\""', '').replace('+', '').replace('.', '')
oppstatrow = str(oppstatrow).replace('tr&gt;', '').replace('th&gt;', '').replace('td&gt;', '').replace('&lt;', '').replace(
    '&gt', '').replace('/', '').replace(';', '').replace('span', '').replace('undermark', '').replace('overermark',
                                                                                                      '').replace(
    'class=', '').replace('\""', '').replace('+', '').replace('.', '')

print(statrow)
print(oppstatrow)
line = re.findall('Overall.+', page)[0]
rec = re.findall('[\d]+\-[\d]+', line)[0]
wl = re.findall('[\d]+', rec)
print("***************TEAM*****************")
win = int(wl[0])
lose = int(wl[1])

line2 = re.findall('PS/G.+', page)[0]
pointsScored = re.findall('[\d]+\.[\d]', line2)[0]
pointsScored = float(pointsScored)
line3 = re.findall('PA/G.+', page)[0]
pointsAllowed = re.findall('[\d]+\.[\d]', line3)[0]
pointsAllowed = float(pointsAllowed)

# total field goals made
fg = re.findall('fg">[\d]+<', statrow)[0]
fg = re.findall('[\d]+', fg)[0]
fg = int(fg)
print(fg)

# total field goal attempts
fga = re.findall('fga">[\d]+<', statrow)[0]
fga = re.findall('[\d]+', fga)[0]
fga = int(fga)
print(fga)

# 2 point field goals
fg2 = re.findall('fg2">[\d]+<', statrow)[0]
fg2 = re.findall('[\d][\d]+', fg2)[0]
fg2 = int(fg2)
print(fg2)

# 2 point field goal attempts
fg2a = re.findall('fg2a">[\d]+<', statrow)[0]
fg2a = re.findall('[\d][\d]+', fg2a)[0]
fg2a = int(fg2a)
print(fg2a)

# 3 point field goals
fg3 = re.findall('fg3">[\d]+<', statrow)[0]
fg3 = re.findall('[\d][\d]+', fg3)[0]
fg3 = int(fg3)
print(fg3)

# 3 point field goal attempts
fg3a = re.findall('fg3a">[\d]+<', statrow)[0]
fg3a = re.findall('[\d][\d]+', fg3a)[0]
fg3a = int(fg3a)
print(fg3a)

# ft field goals
ft = re.findall('ft">[\d]+<', statrow)[0]
ft = re.findall('[\d][\d]+', ft)[0]
ft = int(ft)
print(ft)

# ft field goals attempted
fta = re.findall('fta">[\d]+<', statrow)[0]
fta = re.findall('[\d][\d]+', fta)[0]
fta = int(fta)
print(fta)

# offensive rebounds
orb = re.findall('orb">[\d]+<', statrow)[0]
orb = re.findall('[\d][\d]+', orb)[0]
orb = int(orb)
print(orb)

# defensive rebounds
drb = re.findall('drb">[\d]+<', statrow)[0]
drb = re.findall('[\d][\d]+', drb)[0]
drb = int(drb)
print(drb)

# assists
ast = re.findall('ast">[\d]+<', statrow)[0]
ast = re.findall('[\d][\d]+', ast)[0]
ast = int(ast)
print(ast)

# steals
stl = re.findall('stl">[\d]+<', statrow)[0]
stl = re.findall('[\d][\d]+', stl)[0]
stl = int(stl)
print(stl)

# blocks
blk = re.findall('blk">[\d]+<', statrow)[0]
blk = re.findall('[\d][\d]+', blk)[0]
blk = int(blk)
print(blk)

# turnovers
tov = re.findall('tov">[\d]+<', statrow)[0]
tov = re.findall('[\d][\d]+', tov)[0]
tov = int(tov)
print(tov)

# personal fouls
pf = re.findall('pf">[\d]+<', statrow)[0]
pf = re.findall('[\d][\d]+', pf)[0]
pf = int(pf)
print(pf)






# total rebounds
trb = int(orb) + int(drb)
print(trb)
# total wins
print(win)

# total losses
print(lose)

# average points scored per game
print(pointsScored)

# average points allowed per game
print(pointsAllowed)

print("***************OPPONENT_TEAM*****************")
# total field goals made
opp_fg = re.findall('opp_fg">[\d]+<', oppstatrow)[0]
opp_fg = re.findall('[\d]+', opp_fg)[0]
opp_fg = int(opp_fg)
print(opp_fg)

# total field goal attempts
opp_fga = re.findall('opp_fga">[\d]+<', oppstatrow)[0]
opp_fga = re.findall('[\d]+', opp_fga)[0]
opp_fga = int(opp_fga)
print(opp_fga)

# 2 point field goals
opp_fg2 = re.findall('opp_fg2">[\d]+<', oppstatrow)[0]
opp_fg2 = re.findall('[\d][\d]+', opp_fg2)[0]
opp_fg2 = int(opp_fg2)
print(opp_fg2)

# 2 point field goal attempts
opp_fg2a = re.findall('opp_fg2a">[\d]+<', oppstatrow)[0]
opp_fg2a = re.findall('[\d][\d]+', opp_fg2a)[0]
opp_fg2a = int(opp_fg2a)
print(opp_fg2a)

# 3 point field goals
opp_fg3 = re.findall('opp_fg3">[\d]+<', oppstatrow)[0]
opp_fg3 = re.findall('[\d][\d]+', opp_fg3)[0]
opp_fg3 = int(opp_fg3)
print(opp_fg3)

# 3 point field goal attempts
opp_fg3a = re.findall('opp_fg3a">[\d]+<', oppstatrow)[0]
opp_fg3a = re.findall('[\d][\d]+', opp_fg3a)[0]
opp_fg3a = int(opp_fg3a)
print(opp_fg3a)

# ft field goals
opp_ft = re.findall('opp_ft">[\d]+<', oppstatrow)[0]
opp_ft = re.findall('[\d][\d]+', opp_ft)[0]
opp_ft = int(opp_ft)
print(opp_ft)

# ft field goals attempted
opp_fta = re.findall('opp_fta">[\d]+<', oppstatrow)[0]
opp_fta = re.findall('[\d][\d]+', opp_fta)[0]
opp_fta = int(opp_fta)
print(opp_fta)

# offensive rebounds
opp_orb = re.findall('opp_orb">[\d]+<', oppstatrow)[0]
opp_orb = re.findall('[\d][\d]+', opp_orb)[0]
opp_orb = int(opp_orb)
print(opp_orb)

# defensive rebounds
opp_drb = re.findall('opp_drb">[\d]+<', oppstatrow)[0]
opp_drb = re.findall('[\d][\d]+', opp_drb)[0]
opp_drb = int(opp_drb)
print(opp_drb)

# assists
opp_ast = re.findall('opp_ast">[\d]+<', oppstatrow)[0]
opp_ast = re.findall('[\d][\d]+', opp_ast)[0]
opp_ast = int(opp_ast)
print(opp_ast)

# steals
opp_stl = re.findall('opp_stl">[\d]+<', oppstatrow)[0]
opp_stl = re.findall('[\d][\d]+', opp_stl)[0]
opp_stl = int(opp_stl)
print(opp_stl)

# blocks
opp_blk = re.findall('opp_blk">[\d]+<', oppstatrow)[0]
opp_blk = re.findall('[\d][\d]+', opp_blk)[0]
opp_blk = int(opp_blk)
print(opp_blk)

# turnovers
opp_tov = re.findall('opp_tov">[\d]+<', oppstatrow)[0]
opp_tov = re.findall('[\d][\d]+', opp_tov)[0]
opp_tov = int(opp_tov)
print(opp_tov)

# personal fouls
opp_pf = re.findall('opp_pf">[\d]+<', oppstatrow)[0]
opp_pf = re.findall('[\d][\d]+', opp_pf)[0]
opp_pf = int(opp_pf)
print(opp_pf)
