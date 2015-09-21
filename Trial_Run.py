__author__ = 'brennan.mcnickle'

from bs4 import BeautifulSoup
import urllib3

# Establishing urllib
http = urllib3.PoolManager()
weburl = "http://www.big12sports.com/SportSelect.dbml?&DB_OEM_ID=10410&SPID=13139&SPSID=106580"
r = http.request('GET', weburl)

# Establishing BeautifulSoup
html_doc = r.data
soup = BeautifulSoup(html_doc, 'html.parser')

# Defines the ColumnParse function
def ColumnParse(classType,className):
   data = soup.findAll(classType, className)

   datalist = []
   for td in data:
      data_list = td.getText().strip()
      datalist.append(data_list)
   return datalist

# Returns list of dates from Big12 games
gameDate = ColumnParse("div","date_nowrap")

# Returns list of home teams from Big12 games
homeTeam = ColumnParse("td","home-team")

#Returns list of home scores from Big12 games
homeScores = ColumnParse("td","home-team-score")

#Returns list of away teams from Big12 games
awayTeams = ColumnParse("td","away-team")

#Returns list of away scores from Big12 games
awayScores = ColumnParse("td","away-team-score")

#Returns list of locations from Big12 games
gameLocations = ColumnParse("td","location hidden-phone")

#Returns list of links from Big12 games
data = soup.findAll('a', target="_STATS")

dataLinks = []
for tag in data:
   link = tag['href']
   dataLinks.append(link)




