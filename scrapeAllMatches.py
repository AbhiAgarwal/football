from bs4 import BeautifulSoup
import urllib2

class Matches:
    def __init__(self, year, time, venue, stage, teamOne, result, teamTwo):
        self.year = year
        self.time = time
        self.venue = venue
        self.stage = stage
        self.teamOne = teamOne
        self.result = result
        self.teamTwo = teamTwo
    def printString(self):
        print self.time, self.venue, self.stage, self.teamOne, self.result, self.teamTwo

# From 2010 -> 2014 the tables are different
def getData():
    matchesArray = []
    url = "http://en.wikipedia.org/wiki/List_of_%s_FIFA_World_Cup_matches"
    currentYear = 2010
    while currentYear != 2018:
        soup = BeautifulSoup(urllib2.urlopen(url % str(currentYear)).read())
        currentStage = ""
        for row in soup.findAll('table')[0].findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 6:
                # Time
                time = cells[0].find(text = True)
                # Venue
                if cells[1].find('a'):
                    venue = cells[1].find('a')(text = True)[0]
                else:
                    venue = cells[1].find(text = True)
                # Stage
                if cells[2].find('a'):
                    stage = cells[2].find('a')(text = True)[0]
                else:
                    stage = cells[2].find(text = True)
                currentStage = stage
                # Team 1
                if cells[3].find('a'):
                    teamOne = cells[3].find('a')(text = True)[0]
                else:
                    teamOne = cells[3].find(text = True)
                # Result
                if cells[4].find('a'):
                    result = cells[4].find('a')(text = True)[0]
                else:
                    result = cells[4].find(text = True)
                # Team 2
                if cells[5].find('a'):
                    teamTwo = cells[5].find('a')(text = True)[0]
                else:
                    teamTwo = cells[5].find(text = True)
                newMatch = Matches(currentYear, time, venue, stage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
            elif len(cells) == 5:
                # Time
                time = cells[0].find(text = True)
                # Venue
                if cells[1].find('a'):
                    venue = cells[1].find('a')(text = True)[0]
                else:
                    venue = cells[1].find(text = True)
                # Team 1
                if cells[2].find('a'):
                    teamOne = cells[2].find('a')(text = True)[0]
                else:
                    teamOne = cells[2].find(text = True)
                # Result
                if cells[3].find('a'):
                    result = cells[3].find('a')(text = True)[0]
                else:
                    result = cells[3].find(text = True)
                # Team 2
                if cells[4].find('a'):
                    teamTwo = cells[4].find('a')(text = True)[0]
                else:
                    teamTwo = cells[4].find(text = True)
                # Stage
                stage = currentStage
                newMatch = Matches(currentYear, time, venue, stage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
        currentYear += 4
        print "Year", currentYear, "Scraped"
    return matchesArray

if __name__ == '__main__':
    matchesArray = getData()
    for i in matchesArray:
        i.printString()
