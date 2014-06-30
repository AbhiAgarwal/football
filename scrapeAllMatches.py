from bs4 import BeautifulSoup
import urllib2

class Matches:
    def __init__(self, time, venue, stage, teamOne, result, teamTwo):
        self.time = time
        self.venue = venue
        self.stage = stage
        self.teamOne = teamOne
        self.result = result
        self.teamTwo = teamTwo
    def printString(self):
        print self.time, self.venue, self.stage, self.teamOne, self.result, self.teamTwo

def getData():
    matchesArray = []
    url = "http://en.wikipedia.org/wiki/List_of_2010_FIFA_World_Cup_matches"
    soup = BeautifulSoup(urllib2.urlopen(url).read())
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
            newMatch = Matches(time, venue, stage, teamOne, result, teamTwo)
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
            newMatch = Matches(time, venue, stage, teamOne, result, teamTwo)
            matchesArray.append(newMatch)
    return matchesArray

if __name__ == '__main__':
    matchesArray = getData()
    for i in matchesArray:
        i.printString()
