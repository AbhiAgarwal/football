from bs4 import BeautifulSoup
import urllib2, json, sys, string, re

url = "http://en.wikipedia.org/wiki/%s_FIFA_World_Cup"
currentYear = 1930
endingYear = 1990
soup = BeautifulSoup(urllib2.urlopen(url % str(currentYear)).read())
for row in soup.findAll('div', {"class" : "vevent"}):
    status = 1
    for i in row.findAll('table'):
        if status == 1:
            tr = i.findAll('tr')
            td = tr[0].findAll('td')
            div = td[0].findAll('div')
            text = div[0].find(text = True)
            print text
            status += 1
        elif status == 2:
            tr = i.findAll('tr')
            th = tr[0].findAll('th')
            currentI = 1
            for i in th:
                if currentI == 1:
                    teamOne = i.find('a')(text = True)[0] if i.find('a') else i.find(text = True)
                    currentI += 1
                    print teamOne
                elif currentI == 2:
                    bad_chars = '(){}<>'
                    result = i.find(text = True)
                    rgx = re.compile('[%s]' % bad_chars)
                    result = rgx.sub('', result)
                    currentI += 1
                    print result
                elif currentI == 3:
                    teamTwo = i.find('a')(text = True) if i.find('a') else i.find(text = True)
                    if len(teamTwo) is 1:
                        print teamTwo[0]
                    else:
                        print 'Not Found'
        else:
            tr = i.findAll('tr')
            td = tr[0].findAll('td')
            div = td[0].findAll('div')
            text = div[0].find(text = True)
            print text
            status = 1
