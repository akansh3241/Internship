#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-1  WEB SCRAPING

# 1) Write a python program to display all the header tags from wikipedia.org.

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.
# 
# 

# In[2]:


##Import Modules


# In[3]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[4]:


#Request page source from url


# In[65]:


url = "https://www.imdb.com/chart/top"


# In[99]:


soup= BeautifulSoup(page.content,'html.parser')
Movie__names=[]
Rating=[]
Releasing_Year=[]


# In[100]:


year = soup.find_all('span',class_="secondaryInfo")
year[0:4]


# In[101]:


for i in year:
    Releasing_Year.append(i.get_text().replace("\n",""))
    
Releasing_Year[0:10]


# In[102]:


rating = soup.find_all('td',class_="ratingColumn imdbRating")
rating[0:4]


# In[103]:


for i in rating:
    Rating.append(i.get_text().replace("\n",""))
    
Rating


# In[104]:


movie=soup.find_all('td',class_="titleColumn")
movie[0:4]


# In[105]:


for i in movie:
    name=i.find('a').get_text()
    Movie__names.append(name)
    
Movie__names


# In[106]:


print(len(Movie__names),len(Rating),len(Releasing_Year))


# In[107]:


IMDB=pd.DataFrame({})
IMDB['titles']=Movie__names
IMDB['rating']=Rating
IMDB['year']=Releasing_Year


# In[108]:



IMDB


# In[109]:


IMDB=pd.DataFrame({})
IMDB['titles']=Movie__names[0:100]
IMDB['rating']=Rating[0:100]
IMDB['year']=Releasing_Year[0:100]


# In[110]:


IMDB


# 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ 
# data (i.e. name, rating, year of release) and make data frame.

# In[43]:


##Import Modules
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[111]:


#Request page source from url

page1= requests.get("https://www.imdb.com/india/top-rated-indian-movies/")


# In[113]:


soup1= BeautifulSoup(page1.content,'html.parser')


# In[114]:


Movie_IND_names=[]
IND_Rating=[]
IND_Releasing_Year=[]


# In[115]:


movie1=soup1.find_all('td',class_="titleColumn")
movie1[0:4]


# In[116]:


for i in movie1:
    name=i.find('a').get_text()
    Movie_IND_names.append(name)
    
Movie_IND_names


# In[117]:


r=soup1.find_all(class_="ratingColumn imdbRating")


# In[118]:


for i in r:
    IND_Rating.append(i.get_text().replace("\n"," "))

IND_Rating[0:10]


# In[119]:


y=soup1.find_all('span',class_="secondaryInfo")
y[0:5]


# In[120]:


for i in y:
    IND_Releasing_Year.append(i.get_text().replace("\n"," "))
IND_Releasing_Year[0:10]


# In[121]:


IND_movies=pd.DataFrame([])
IND_movies['Movie_Name']=Movie_IND_names
IND_movies['IMDB_Rating']=IND_Rating
IND_movies['Year_of_Release']=IND_Releasing_Year


# In[122]:


IND_movies[0:10]


# In[123]:


IND_movies=pd.DataFrame([])
IND_movies['Movie_Name']=Movie_IND_names[0:100]
IND_movies['IMDB_Rating']=IND_Rating[0:100]
IND_movies['Year_of_Release']=IND_Releasing_Year[0:100]


# In[124]:


IND_movies


# 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[76]:


import requests
r = requests.get('https://presidentofindia.nic.in/former-presidents.htm')

print(r.text[0:500])


# In[77]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')


# In[78]:


results = soup.find_all('span', attrs={'class':'short-desc'})


# In[79]:


len(results)


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.
# 

# # Men's ODI Team Rankings

# In[125]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[126]:


page= requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[129]:


soup= BeautifulSoup(page.content,'html.parser')


# In[130]:


Team=[]
Matches=[]
Points=[]
Rating=[]


# In[131]:


Country = soup.find_all('span',class_="u-hide-phablet")
Country[0:4]


# In[132]:


for i in Country:
    Team.append(i.get_text().replace("\n",""))
    
Team=Team[0:10]
Team


# In[133]:


match=soup.find_all('td',class_='rankings-block__banner--matches')

matchs=soup.find_all('td',class_='table-body__cell u-center-text')

mtc = match + matchs

for i in mtc:
    Matches.append(i.text)
    Matches=Matches[0:10]


# In[134]:


Matches


# In[135]:


pt=soup.find_all('td',class_="rankings-block__banner--points")

pts= soup.find_all('td',class_ ="table-body__cell u-center-text")
Point= pt + pts


# In[136]:


for i in Point:
   Points.append(i.get_text().replace("\n",""))
   Points=Points[0:10]


# In[137]:


rating = soup.find_all('td',class_="table-body__cell u-text-right rating")
rating[0:4]


# In[138]:


for i in rating:
    Rating.append(i.get_text().replace("\n",""))
    Rating=Rating[0:10]


# In[139]:


print(len(Team),len(Rating),len(Points))


# In[140]:


ODI=pd.DataFrame({})
ODI['Country']=Team
ODI['Matches']=Matches
ODI['Rating']=Rating
ODI['Points']=Points


# In[141]:


ODI


# # Men's ODI Batsman-Player Rankings

# In[142]:


Page1= requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")


# In[143]:


Page1


# In[144]:


Soup1= BeautifulSoup(Page1.content,'html.parser')


# In[145]:


TEAM=[]
RATING=[]
Player=[]


# In[146]:


P1 = Soup1.find_all('div',class_="rankings-block__banner--name-large")

P9=Soup1.find_all('td',class_="table-body__cell rankings-table__name name")
PLAYERS=P1+P9
PLAYERS


# In[147]:


for i in PLAYERS:
    Player.append(i.get_text().replace("\n",""))
    Player=Player[0:10]
Player


# In[148]:


T1=Soup1.find_all('div',class_='rankings-block__banner--nationality')

T9=Soup1.find_all('span',class_='table-body__logo-text')

TEAMS = T1 + T9

for i in TEAMS:
    TEAM.append(i.get_text().replace("\n",""))
    TEAM=TEAM[0:10]
    
TEAM


# In[149]:


r1 = Soup1.find_all('div',class_="rankings-block__banner--rating")

r9 = Soup1.find_all('td',class_="table-body__cell rating")

rating=r1+r9
rating[0:10]


# In[150]:


for i in rating:
    RATING.append(i.get_text().replace("\n",""))
    
RATING=RATING[0:10]
RATING


# In[151]:


ODI_B=pd.DataFrame({})
ODI_B['Country']=TEAM
ODI_B['Player']=Player
ODI_B['Rating']=RATING


# In[152]:


ODI_B


# # Men's ODI Bowler-Player Rankings

# In[153]:


Page2= requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")


# In[154]:


Soup2= BeautifulSoup(Page2.content,'html.parser')


# In[155]:


B_TEAM=[]
B_RATING=[]
B_Player=[]


# In[156]:


BP1 = Soup2.find_all('div',class_="rankings-block__banner--name-large")

BP9=Soup2.find_all('td',class_="table-body__cell rankings-table__name name")
BPLAYERS=BP1+BP9
BPLAYERS


# In[157]:


for i in BPLAYERS:
    B_Player.append(i.get_text().replace("\n",""))
    B_Player=B_Player[0:10]
B_Player


# In[158]:


BT1=Soup2.find_all('div',class_='rankings-block__banner--nationality')

BT9=Soup2.find_all('span',class_='table-body__logo-text')

BTEAMS = BT1 + BT9


# In[159]:


for i in BTEAMS:
    B_TEAM.append(i.get_text().replace("\n",""))
    B_TEAM=B_TEAM[0:10]
    
B_TEAM


# In[160]:


Br1 = Soup2.find_all('div',class_="rankings-block__banner--rating")

Br9 = Soup2.find_all('td',class_="table-body__cell rating")

Brating=Br1+Br9
Brating[0:10]


# In[161]:


for i in Brating:
    B_RATING.append(i.get_text().replace("\n",""))
    
B_RATING=B_RATING[0:10]
B_RATING


# In[162]:


ODI_Bow=pd.DataFrame({})
ODI_Bow['Country']=B_TEAM
ODI_Bow['Player']=B_Player
ODI_Bow['Rating']=B_RATING


# In[163]:


ODI_Bow


# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# # Women's ODI Team Rankings

# In[164]:


PAGE= requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")

PAGE.content

SOUP= BeautifulSoup(PAGE.content,'html.parser')


# In[165]:


W_Team=[]
W_Matches=[]
W_Points=[]
W_Rating=[]


# In[166]:


WCountry = SOUP.find_all('span',class_="u-hide-phablet")
WCountry[0:4]


# In[167]:


for i in WCountry:
    W_Team.append(i.get_text().replace("\n",""))
    
W_Team=W_Team[0:10]
W_Team


# In[168]:


Wmatch=SOUP.find_all('td',class_='rankings-block__banner--matches')

Wmatchs=SOUP.find_all('td',class_='table-body__cell u-center-text')

Wmtc = Wmatch + Wmatchs


# In[169]:


for i in  Wmtc:
    W_Matches.append(i.text)
    W_Matches=W_Matches[0:10]
    

W_Matches


# In[170]:


Wpt=SOUP.find_all('td',class_="rankings-block__banner--points")

Wpts= SOUP.find_all('td',class_ ="table-body__cell u-center-text")
WPoint= Wpt + Wpts


# In[171]:


for i in WPoint:
    W_Points.append(i.get_text().replace("\n",""))
    W_Points=W_Points[0:10]
W_Points


# In[172]:


rat=SOUP.find_all('td',class_="rankings-block__banner--rating")

Wrating = SOUP.find_all('td',class_="table-body__cell u-text-right rating")
WRATING=rat + Wrating


# In[173]:


for i in WRATING:
    W_Rating.append(i.get_text().replace("\n",""))
    W_Rating=W_Rating[0:10]
W_Rating


# In[174]:


print(len(W_Team),len(W_Rating),len(W_Points))


# In[175]:


WODI=pd.DataFrame({})
WODI['Country']=W_Team
WODI['Matches']=W_Matches
WODI['Rating']=W_Rating
WODI['Points']=W_Points

WODI


# # Women's ODI Batsman-Player Rankings

# In[176]:


PAGE1= requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")


# In[177]:


SOUP1= BeautifulSoup(PAGE1.content,'html.parser')


# In[178]:


W_TEAM=[]
W_RATING=[]
W_Player=[]


# In[179]:


WP1 = SOUP1.find_all('div',class_="rankings-block__banner--name-large")

WP9=SOUP1.find_all('td',class_="table-body__cell rankings-table__name name")
WPLAYERS=WP1+WP9
WPLAYERS


# In[180]:


for i in WPLAYERS:
    W_Player.append(i.get_text().replace("\n",""))
    W_Player=W_Player[0:10]
W_Player


# In[181]:


WT1=SOUP1.find_all('div',class_='rankings-block__banner--nationality')

WT9=SOUP1.find_all('span',class_='table-body__logo-text')

WTEAMS = WT1 + WT9

WTEAMS


# In[182]:


for i in WTEAMS:
    W_TEAM.append(i.get_text().replace("\n",""))
    W_TEAM=W_TEAM[0:10]
    
W_TEAM


# In[183]:


Wr1 = SOUP1.find_all('div',class_="rankings-block__banner--rating")

Wr9 = SOUP1.find_all('td',class_="table-body__cell rating")

Wrating=Wr1+Wr9
Wrating[0:10]


# In[184]:


for i in Wrating:
    W_RATING.append(i.get_text().replace("\n",""))
    
W_RATING=W_RATING[0:10]
W_RATING


# In[185]:


WODI_B=pd.DataFrame({})
WODI_B['Country']=W_TEAM
WODI_B['Player']=W_Player
WODI_B['Rating']=W_RATING


# In[186]:


WODI_B


# # Women's ODI All Rounder Rankings

# In[187]:


PAGE2= requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling")


# In[188]:


SOUP2= BeautifulSoup(PAGE2.content,'html.parser')


# In[189]:


WB_TEAM=[]
WB_RATING=[]
WB_Player=[]


# In[190]:


WBP1 = SOUP2.find_all('div',class_="rankings-block__banner--name-large")

WBP9=SOUP2.find_all('td',class_="table-body__cell rankings-table__name name")
WBPLAYERS=WBP1+WBP9
WBPLAYERS


# In[191]:


for i in WBPLAYERS:
    WB_Player.append(i.get_text().replace("\n",""))
    WB_Player=WB_Player[0:10]
WB_Player


# In[192]:


WBT1=SOUP2.find_all('div',class_='rankings-block__banner--nationality')

WBT9=SOUP2.find_all('span',class_='table-body__logo-text')

WBTEAMS = WBT1 + WBT9


# In[193]:


for i in WBTEAMS:
    WB_TEAM.append(i.get_text().replace("\n",""))
    WB_TEAM=WB_TEAM[0:10]
    
WB_TEAM


# In[194]:


WBr1 = SOUP2.find_all('div',class_="rankings-block__banner--rating")

WBr9 = SOUP2.find_all('td',class_="table-body__cell rating")

WBrating=WBr1+WBr9
WBrating[0:10]


# In[195]:


for i in WBrating:
    WB_RATING.append(i.get_text().replace("\n",""))
    
WB_RATING=WB_RATING[0:10]
WB_RATING


# In[196]:


WODI_Bow=pd.DataFrame({})
WODI_Bow['Country']=WB_TEAM
WODI_Bow['Player']=WB_Player
WODI_Bow['Rating']=WB_RATING


# In[197]:


WODI_Bow

