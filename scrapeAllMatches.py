from bs4 import BeautifulSoup
import urllib2, json

futureYear = 2014 + 4

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
        print self.year, self.time, self.venue, self.stage, self.teamOne, self.result, self.teamTwo

def get1930PostData():
    matchesARray = []
    url = "http://en.wikipedia.org/wiki/%s_FIFA_World_Cup"
    currentYear = 1930
    limitYear = 1990
    while currentYear != limitYear:

        print "Year", currentYear, "Scraped"
        currentYear += 4

# From 1990 -> 2006 the tables are different
def get2010PreData():
    matchesArray = []
    url = "http://en.wikipedia.org/wiki/List_of_%s_FIFA_World_Cup_matches"
    currentYear = 1990
    limitYear = 2010
    while currentYear != limitYear:
        soup = BeautifulSoup(urllib2.urlopen(url % str(currentYear)).read())
        currentStage = ""
        for row in soup.findAll('table')[0].findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 5:
                # Time
                time = cells[0].find(text = True)
                # Stage
                currentStage = stage = cells[1].find('a')(text = True)[0] if cells[1].find('a') else cells[1].find(text = True)
                # Team 1
                teamOne = cells[2].find('a')(text = True)[0] if cells[2].find('a') else cells[2].find(text = True)
                # Result
                result = cells[3].find('a')(text = True)[0] if cells[3].find('a') else cells[3].find(text = True)
                # Team 2
                teamTwo = cells[4].find('a')(text = True)[0] if cells[4].find('a') else cells[4].find(text = True)
                # Save and Append
                newMatch = Matches(currentYear, time, '', stage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
            elif len(cells) == 4:
                # When 4: Means that the stage is currently missing, so we have to import it from the last one
                # Time
                time = cells[0].find(text = True)
                # Team 1
                teamOne = cells[1].find('a')(text = True)[0] if cells[1].find('a') else cells[1].find(text = True)
                # Result
                result = cells[2].find('a')(text = True)[0] if cells[2].find('a') else cells[2].find(text = True)
                # Team 2
                teamTwo = cells[3].find('a')(text = True)[0] if cells[3].find('a') else cells[3].find(text = True)
                # Save
                newMatch = Matches(currentYear, time, '', currentStage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
        print "Year", currentYear, "Scraped"
        currentYear += 4
    return matchesArray

# From 2010 -> 2014 the tables are different
def get2010PostData():
    matchesArray = []
    url = "http://en.wikipedia.org/wiki/List_of_%s_FIFA_World_Cup_matches"
    currentYear = 2010
    while currentYear != futureYear:
        soup = BeautifulSoup(urllib2.urlopen(url % str(currentYear)).read())
        currentStage = ""
        for row in soup.findAll('table')[0].findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 6:
                # Time
                time = cells[0].find(text = True)
                # Venue
                venue = cells[1].find('a')(text = True)[0] if cells[1].find('a') else cells[1].find(text = True)
                # Stage
                currentStage = stage = cells[2].find('a')(text = True)[0] if cells[2].find('a') else cells[2].find(text = True)
                # Team 1
                teamOne = cells[3].find('a')(text = True)[0] if cells[3].find('a') else cells[3].find(text = True)
                # Result
                result = cells[4].find('a')(text = True)[0] if cells[4].find('a') else cells[4].find(text = True)
                # Team 2
                teamTwo = cells[5].find('a')(text = True)[0] if cells[5].find('a') else cells[5].find(text = True)
                # Save
                newMatch = Matches(currentYear, time, venue, stage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
            elif len(cells) == 5:
                # Time
                time = cells[0].find(text = True)
                # Venue
                venue = cells[1].find('a')(text = True)[0] if cells[1].find('a') else cells[1].find(text = True)
                # Team 1
                teamOne = cells[2].find('a')(text = True)[0] if cells[2].find('a') else cells[2].find(text = True)
                # Result
                result = cells[3].find('a')(text = True)[0] if cells[3].find('a') else cells[3].find(text = True)
                # Team 2
                teamTwo = cells[4].find('a')(text = True)[0] if cells[4].find('a') else cells[4].find(text = True)
                # Save
                newMatch = Matches(currentYear, time, venue, currentStage, teamOne, result, teamTwo)
                matchesArray.append(newMatch)
        print "Year", currentYear, "Scraped"
        currentYear += 4
    return matchesArray

def createJSON(matchesArray):
    fullJSON = []
    for i in matchesArray:
        fullJSON.append({
            'Year': i.year,
            'Time': i.time,
            'Venue': i.venue,
            'Stage': i.stage,
            'Team 1': i.teamOne,
            'Result': i.result,
            'Team 2': i.teamTwo
        })
    return fullJSON

if __name__ == '__main__':
    matchesArray = get2010PreData()
    matchesArray += get2010PostData()
    # Prepare JSON data
    jsonData = createJSON(matchesArray)
    fullData = json.dumps(jsonData, ensure_ascii=False, encoding='utf8')
    # Write JSON data
    fd = open('./data/worldCupMatches.json', 'w')
    fd.write(fullData.encode('utf-8'))
    fd.close()
