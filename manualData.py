import json

twenty_ten = []

def appendToArray(teamOne, teamTwo, scoreOne, scoreTwo):
    twenty_ten.append({
        'Teams': [teamOne, teamTwo],
        'Result': [scoreOne, scoreTwo]
    })

if __name__ == '__main__':
    # First round of group stage matches
    appendToArray('South Africa', 'Mexico', 1, 1)
    appendToArray('Uruguay', 'France', 0, 0)
    appendToArray('South Korea', 'Greece', 2, 0)
    appendToArray('Argentina', 'Nigeria', 1, 0)
    appendToArray('England', 'United States', 1, 1)
    appendToArray('Algeria', 'Slovenia', 0, 1)
    appendToArray('Serbia', 'Ghana', 0, 1)
    appendToArray('Germany', 'Australia', 4, 0)
    appendToArray('Netherlands', 'Denmark', 2, 0)
    appendToArray('Japan', 'Cameroon', 1, 0)
    appendToArray('Italy', 'Paraguay', 1, 1)
    appendToArray('New Zealand', 'Slovakia', 1, 1)
    appendToArray('Ivory Coast', 'Portugal', 0, 0)
    appendToArray('Brazil', 'North Korea', 2, 1)
    appendToArray('Honduras', 'Chile', 0, 1)
    appendToArray('Spain', 'Switzerland', 0, 1)

    fullData = json.dumps(twenty_ten)
    print 'JSON:', fullData
