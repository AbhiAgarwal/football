from bs4 import BeautifulSoup
import urllib2

wiki = "http://en.wikipedia.org/wiki/List_of_2010_FIFA_World_Cup_matches"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki, headers = header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

table = soup.find("table", { "class" : "wikitable" })

day, time, venue, stage, teamOne, teamTwo, result = "", "", "", "", "", "", ""

currentDay = ""

for row in table.findAll("tr"):
    date = row.findAll("th")
    # for i in date:
        # print i.find(text = True)
    cells = row.findAll("td")
    for i in cells:
        print i.find(text = True)
