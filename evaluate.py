import json, unicodedata

# Finds all games for a set of countries
def findAllGamesForGroup(matches, country):
    toReturn = []
    for i in matches:
        if i['Against'] == country:
            toReturn.append(i)
    return toReturn

# Checks how many countries there are that the a country has played
# more than just once
def findNumberOfMultipleGames(matches):
    toCheck = {}
    toReturn = 0
    for i in matches:
        if i['Against'] in toCheck:
            toReturn += 1
        else:
            toCheck[(i['Against'])] = 1
    return toReturn

# Checks if a country has played against another
def playedAgainst(matches, country):
    if findAllGamesForGroup(matches, country):
        return True
    else:
        return False

# Evaluation to see which country would win given a set of them
def evaluate(year, matches, current):
    # print findAllGamesForGroup(matches['Germany'], u'Sweden')
    # print findNumberOfMultipleGames(matches['Germany'])
    # print playedAgainst(matches['Germany'], u'United States')
    print findAllGamesForGroup(matches['Brazil'], u'Colombia')
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
        yearWinner[i['Year']] = {'Winner': i['Winner'], 'Runner-up': i['Runners-up'], 'Final Score': finalScore}
    for i in allMatches:
        if i['Year'] != 2014:
            # Old technique to use a tuple to group the teams together
            # in the dictionary, but lets not go this way.
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
            # Evaluating the result
            # Grouping each country together, and cutting out some details
            # we don't need for evaluation.
            m = {'Result': i['Result'], 'Against': i['Team 2'], 'Year': i['Year']}
            n = {'Result': i['Result'], 'Against': i['Team 1'], 'Year': i['Year']}
            if (i['Team 1']) in matches:
                matches[(i['Team 1'])].append(m)
            else:
                matches[(i['Team 1'])] = []
                matches[(i['Team 1'])].append(m)
            if (i['Team 2']) in matches:
                matches[(i['Team 2'])].append(n)
            else:
                matches[(i['Team 2'])] = []
                matches[(i['Team 2'])].append(n)
        else:
            current.append(i)
    evaluate(yearWinner, matches, current)
