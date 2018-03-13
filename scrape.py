from bs4 import BeautifulSoup

import requests

import re
import csv

# team = input("Enter team to get record for: ")
teamstats = open("teamstats.csv",'w')

with open("teams-2018.txt") as teamsheet:
    lines=teamsheet.readlines()
    for thing in lines:
        team = thing.rstrip()
        print(team)
        r = requests.get("http://sports-reference.com/cbb/schools/" + team + "/2018.html")

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        # Find all of the text between paragraph tags and strip out the html
        page = soup.getText()

        line = re.findall('Overall.+', page)[0]
        rec = re.findall('[\d]+\-[\d]+', line)[0]
        wl = re.findall('[\d]+', rec)
        win = wl[0]
        lose = wl[1]

        line2 = re.findall('PS/G.+', page)[0]
        pointsScored = re.findall('[\d]+\.[\d]', line2)[0]
        line3 = re.findall('PA/G.+', page)[0]
        pointsAllowed = re.findall('[\d]+\.[\d]', line3)[0]

        # Print Page
        print(line)
        print(rec)
        print(win)
        print(lose)
        print(pointsScored)
        print(pointsAllowed)
        teamstats.write(team+","+win+","+lose+","+pointsScored+","+pointsAllowed+"\n")
