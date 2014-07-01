import json, unicodedata

def evaluate(year, matches, current):
    pass

if __name__ == '__main__':
    # yearWinner -> Dictionary for winner of each year
    # winners -> List from JSON file of all the winners
    # allMatches -> List from JSON file of all the matches 1990 -> 2014
    # matches -> Dictionary for all matches played by a country
    # current -> List of all games played in 2014
    yearWinner, winners, allMatches, matches, current = {}, [], [], {}, []
    with open('./data/worldCupFinals.json') as data_file:
        winners = json.load(data_file)
    with open('./data/worldCupMatches.json') as data_file:
        allMatches = json.load(data_file)
    for i in winners:
        finalScore = u"{0}".format(i['Final Score'])
        yearWinner[i['Year']] = i
    for i in allMatches:
        if i['Year'] != 2014:
            '''
            if (i['Team 1'], i['Team 2']) in matches or (i['Team 2'], i['Team 1']) in matches:
                if (i['Team 2'], i['Team 1']) in matches:
                    matches[(i['Team 2'], i['Team 1'])].append(i)
                else:
                    matches[(i['Team 1'], i['Team 2'])].append(i)

                if (i['Team 2'], i['Team 1']) in matches and (i['Team 1'], i['Team 2']) in matches:
                    matches[(i['Team 1'], i['Team 2'])] += matches[(i['Team 2'], i['Team 1'])]
                    del matches[(i['Team 2'], i['Team 1'])]
            else:
                matches[(i['Team 1'], i['Team 2'])] = []
                matches[(i['Team 1'], i['Team 2'])].append(i)
            '''
            if (i['Team 1']) in matches:
                matches[(i['Team 1'])].append(i)
            else:
                matches[(i['Team 1'])] = []
                matches[(i['Team 1'])].append(i)

            if (i['Team 2']) in matches:
                matches[(i['Team 2'])].append(i)
            else:
                matches[(i['Team 2'])] = []
                matches[(i['Team 2'])].append(i)
        else:
            current.append(i)
    print (matches['Germany'])
    evaluate(yearWinner, matches, current)
