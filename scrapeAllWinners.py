from bs4 import BeautifulSoup
import urllib2, json, io

url = "http://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"
soup = BeautifulSoup(urllib2.urlopen(url).read())

class Matches:
    def __init__(self, currentYear, winner, finalScore, runnerUp, venue, location, attendance):
        self.year = currentYear
        self.winner = winner
        self.finalScore = finalScore
        self.runnerUp = runnerUp
        self.venue = venue
        self.location = location
        self.attendance = attendance
    def printString(self):
        print self.year, self.winner, self.finalScore, self.runnerUp, self.venue, self.location, self.attendance

def getData():
    matchesArray = []
    currentYear = 1930
    for row in soup.findAll('table')[2].findAll('tr'):
        cells = row.findAll('td')
        if len(cells) == 7:
            # Winner
            if cells[0].find('a'):
                winner = cells[0].find('a')(text = True)[0]
            else:
                winner = cells[0].find(text = True)
            # Final Score
            if cells[1].find('a'):
                finalScore = cells[1].find('a')(text = True)[0]
            else:
                finalScore = cells[1].find(text = True)
            # Runners-up
            if cells[2].find('a'):
                runnerUp = cells[2].find('a')(text = True)[0]
            else:
                runnerUp = cells[2].find(text = True)
            # Venue
            if cells[3].find('a'):
                venue = cells[3].find('a')(text = True)[0]
            else:
                venue = cells[3].find(text = True)
            # Location
            if cells[4].find('a'):
                location = cells[4].find('a')(text = True)[0]
            else:
                location = cells[4].find(text = True)
            # Attendance
            if cells[5].find('a'):
                attendance = cells[5].find(text = True)
            else:
                attendance = cells[5].find(text = True)

            newMatch = Matches(currentYear, winner, finalScore, runnerUp, venue, location, attendance)
            matchesArray.append(newMatch)

            currentYear += 4

            # The aftermath of World War II also caused the cancellation of the 1946 tournament.
            if currentYear == 1942:
                currentYear = 1950
    return matchesArray

def getJSON(matchesArray):
    fullJSON = []
    for i in matchesArray:
        fullJSON.append({
            'Year': i.year,
            'Winner': i.winner,
            'Final Score': i.finalScore,
            'Runners-up': i.runnerUp,
            'Venue': i.venue,
            'Location': i.location,
            'Attendance': i.attendance
        })
    return fullJSON

if __name__ == '__main__':
    matchesArray = getData()
    jsonData = getJSON(matchesArray)
    fullData = json.dumps(jsonData, ensure_ascii=False, encoding='utf8')

    # write json
    fd = open('./data/worldCupFinals.json', 'w')
    fd.write(fullData.encode('utf-8'))
    fd.close()
