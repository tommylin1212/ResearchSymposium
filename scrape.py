from bs4 import BeautifulSoup

import requests

import re
import csv

year = input("Enter year to get record for: ")
teamstats = open("teamstats2018.csv", 'w')
teamstats.write(
    "team" + "," + "win" + "," + "lose" + "," + "pointsScored" + "," + "pointsAllowed"
    + "," + "fg" + "," + "fga" + "," + "fg2" + "," + "fg2a" + "," + "fg3" + "," + "fg3a" + "," + "ft" + ","
    + "fta" + "," + "orb" + "," + "drb" + "," + "ast" + "," + "stl" + "," + "blk" + "," + "tov"
    + "," + "pf" + "," + "opp_fg" + "," + "opp_fga" + "," + "opp_fg2" + "," + "opp_fg2a" + "," + "opp_fg3"
    + "," + "opp_fg3a" + "," + "opp_ft" + "," + "opp_ft" + "," + "opp_orb" + "," + "opp_drb" + ","
    + "opp_ast" + "," + "opp_stl" + "," + "opp_blk" + "," + "opp_tov" + "," + "opp_pf"+'\n')
with open("teams-2018.txt") as teamsheet:
    lines = teamsheet.readlines()
    for thing in lines:
        team = thing.rstrip()
        print(team)

        r = requests.get("http://sports-reference.com/cbb/schools/" + team + "/2018.html")

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        # Find all of the text between paragraph tags and strip out the html
        page = soup.getText()

        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "team_stats")
        rows = table.findAll(lambda tag: tag.name == 'tr')
        num = len(rows) - 4
        statrow = rows[num]
        oppstatrow = rows[num + 2]

        statrow = str(statrow).replace('tr&gt;', '').replace('th&gt;', '').replace('td&gt;', '').replace('&lt;',
                                                                                                         '').replace(
            '&gt', '').replace('/', '').replace(';', '').replace('span', '').replace('undermark', '').replace(
            'overermark',
            '').replace(
            'class=', '').replace('\""', '').replace('+', '').replace('.', '')
        oppstatrow = str(oppstatrow).replace('tr&gt;', '').replace('th&gt;', '').replace('td&gt;', '').replace('&lt;',
                                                                                                               '').replace(
            '&gt', '').replace('/', '').replace(';', '').replace('span', '').replace('undermark', '').replace(
            'overermark',
            '').replace(
            'class=', '').replace('\""', '').replace('+', '').replace('.', '')

        print(statrow)
        print(oppstatrow)
        line = re.findall('Overall.+', page)[0]
        rec = re.findall('[\d]+\-[\d]+', line)[0]
        wl = re.findall('[\d]+', rec)
        print("***************TEAM*****************")
        win = wl[0]
        lose = wl[1]

        line2 = re.findall('PS/G.+', page)[0]
        pointsScored = re.findall('[\d]+\.[\d]', line2)[0]

        line3 = re.findall('PA/G.+', page)[0]
        pointsAllowed = re.findall('[\d]+\.[\d]', line3)[0]

        # total field goals made
        fg = re.findall('fg">[\d]+<', statrow)[0]
        fg = re.findall('[\d]+', fg)[0]

        print(fg)

        # total field goal attempts
        fga = re.findall('fga">[\d]+<', statrow)[0]
        fga = re.findall('[\d]+', fga)[0]

        print(fga)

        # 2 point field goals
        fg2 = re.findall('fg2">[\d]+<', statrow)[0]
        fg2 = re.findall('[\d][\d]+', fg2)[0]

        print(fg2)

        # 2 point field goal attempts
        fg2a = re.findall('fg2a">[\d]+<', statrow)[0]
        fg2a = re.findall('[\d][\d]+', fg2a)[0]

        print(fg2a)

        # 3 point field goals
        fg3 = re.findall('fg3">[\d]+<', statrow)[0]
        fg3 = re.findall('[\d][\d]+', fg3)[0]

        print(fg3)

        # 3 point field goal attempts
        fg3a = re.findall('fg3a">[\d]+<', statrow)[0]
        fg3a = re.findall('[\d][\d]+', fg3a)[0]

        print(fg3a)

        # ft field goals
        ft = re.findall('ft">[\d]+<', statrow)[0]
        ft = re.findall('[\d][\d]+', ft)[0]

        print(ft)

        # ft field goals attempted
        fta = re.findall('fta">[\d]+<', statrow)[0]
        fta = re.findall('[\d][\d]+', fta)[0]

        print(fta)

        # offensive rebounds
        orb = re.findall('orb">[\d]+<', statrow)[0]
        orb = re.findall('[\d][\d]+', orb)[0]

        print(orb)

        # defensive rebounds
        drb = re.findall('drb">[\d]+<', statrow)[0]
        drb = re.findall('[\d][\d]+', drb)[0]

        print(drb)

        # assists
        ast = re.findall('ast">[\d]+<', statrow)[0]
        ast = re.findall('[\d][\d]+', ast)[0]

        print(ast)

        # steals
        stl = re.findall('stl">[\d]+<', statrow)[0]
        stl = re.findall('[\d][\d]+', stl)[0]

        print(stl)

        # blocks
        blk = re.findall('blk">[\d]+<', statrow)[0]
        blk = re.findall('[\d][\d]+', blk)[0]

        print(blk)

        # turnovers
        tov = re.findall('tov">[\d]+<', statrow)[0]
        tov = re.findall('[\d][\d]+', tov)[0]

        print(tov)

        # personal fouls
        pf = re.findall('pf">[\d]+<', statrow)[0]
        pf = re.findall('[\d][\d]+', pf)[0]

        print(pf)

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

        print(opp_fg)

        # total field goal attempts
        opp_fga = re.findall('opp_fga">[\d]+<', oppstatrow)[0]
        opp_fga = re.findall('[\d]+', opp_fga)[0]

        print(opp_fga)

        # 2 point field goals
        opp_fg2 = re.findall('opp_fg2">[\d]+<', oppstatrow)[0]
        opp_fg2 = re.findall('[\d][\d]+', opp_fg2)[0]

        print(opp_fg2)

        # 2 point field goal attempts
        opp_fg2a = re.findall('opp_fg2a">[\d]+<', oppstatrow)[0]
        opp_fg2a = re.findall('[\d][\d]+', opp_fg2a)[0]

        print(opp_fg2a)

        # 3 point field goals
        opp_fg3 = re.findall('opp_fg3">[\d]+<', oppstatrow)[0]
        opp_fg3 = re.findall('[\d][\d]+', opp_fg3)[0]

        print(opp_fg3)

        # 3 point field goal attempts
        opp_fg3a = re.findall('opp_fg3a">[\d]+<', oppstatrow)[0]
        opp_fg3a = re.findall('[\d][\d]+', opp_fg3a)[0]

        print(opp_fg3a)

        # ft field goals
        opp_ft = re.findall('opp_ft">[\d]+<', oppstatrow)[0]
        opp_ft = re.findall('[\d][\d]+', opp_ft)[0]

        print(opp_ft)

        # ft field goals attempted
        opp_fta = re.findall('opp_fta">[\d]+<', oppstatrow)[0]
        opp_fta = re.findall('[\d][\d]+', opp_fta)[0]

        print(opp_fta)

        # offensive rebounds
        opp_orb = re.findall('opp_orb">[\d]+<', oppstatrow)[0]
        opp_orb = re.findall('[\d][\d]+', opp_orb)[0]

        print(opp_orb)

        # defensive rebounds
        opp_drb = re.findall('opp_drb">[\d]+<', oppstatrow)[0]
        opp_drb = re.findall('[\d][\d]+', opp_drb)[0]

        print(opp_drb)

        # assists
        opp_ast = re.findall('opp_ast">[\d]+<', oppstatrow)[0]
        opp_ast = re.findall('[\d][\d]+', opp_ast)[0]

        print(opp_ast)

        # steals
        opp_stl = re.findall('opp_stl">[\d]+<', oppstatrow)[0]
        opp_stl = re.findall('[\d][\d]+', opp_stl)[0]

        print(opp_stl)

        # blocks
        opp_blk = re.findall('opp_blk">[\d]+<', oppstatrow)[0]
        opp_blk = re.findall('[\d][\d]+', opp_blk)[0]

        print(opp_blk)

        # turnovers
        opp_tov = re.findall('opp_tov">[\d]+<', oppstatrow)[0]
        opp_tov = re.findall('[\d][\d]+', opp_tov)[0]

        print(opp_tov)

        # personal fouls
        opp_pf = re.findall('opp_pf">[\d]+<', oppstatrow)[0]
        opp_pf = re.findall('[\d][\d]+', opp_pf)[0]

        print(opp_pf)
        teamstats.write(
            team + "," + win + "," + lose + "," + pointsScored + "," + pointsAllowed
            + "," + fg + "," + fga + "," + fg2 + "," + fg2a + "," + fg3 + "," + fg3a + "," + ft + ","
            + fta + "," + orb + "," + drb + "," + ast + "," + stl + "," + blk + "," + tov
            + "," + pf + "," + opp_fg + "," + opp_fga + "," + opp_fg2 + "," + opp_fg2a + "," + opp_fg3
            + "," + opp_fg3a + "," + opp_ft + "," + opp_ft + "," + opp_orb + "," + opp_drb + ","
            + opp_ast + "," + opp_stl + "," + opp_blk + "," + opp_tov + "," + opp_pf + '\n')
