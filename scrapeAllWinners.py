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
            winner = cells[0].find('a')(text = True)[0] if cells[0].find('a') else cells[0].find(text = True)
            # Final Score
            finalScore = cells[1].find('a')(text = True)[0] if cells[1].find('a') else cells[1].find(text = True)
            # Runners-up
            runnerUp = cells[2].find('a')(text = True)[0] if cells[2].find('a') else cells[2].find(text = True)
            # Venue
            venue = cells[3].find('a')(text = True)[0] if cells[3].find('a') else cells[3].find(text = True)
            # Location
            location = cells[4].find('a')(text = True)[0] if cells[4].find('a') else cells[4].find(text = True)
            # Attendance
            attendance = cells[5].find('a')(text = True)[0] if cells[5].find('a') else cells[5].find(text = True)
            # Save
            newMatch = Matches(currentYear, winner, finalScore, runnerUp, venue, location, attendance)
            matchesArray.append(newMatch)
            # The aftermath of World War II also caused the cancellation of the 1946 tournament.
            currentYear += 4
            if currentYear == 1942:
                currentYear = 1950
    return matchesArray

def createJSON(matchesArray):
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
    jsonData = createJSON(matchesArray)
    fullData = json.dumps(jsonData, ensure_ascii=False, encoding='utf8')

    # write json
    fd = open('./data/worldCupFinals.json', 'w')
    fd.write(fullData.encode('utf-8'))
    fd.close()
