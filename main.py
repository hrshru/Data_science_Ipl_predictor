import requests
from bs4 import BeautifulSoup
import pandas as pd


#top-batsman record

URL='https://www.iplt20.com/stats/2020/most-runs'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('div', attrs = {'class':'js-table'})

player_info={}
player_name_lst=[]
total_match_lst=[]
total_inngs_lst=[]
runs_lst=[]
hs_lst=[]
avg_lst=[]
sr_lst=[]
for row in table.findAll('table', attrs={'table table--scroll-on-tablet top-players'}):
    for j in row.findAll('div', attrs={'class':"top-players__player-name"}):
        player_name_lst.append(j.a['href'].split('/')[-1])
    for match in row.findAll('td',attrs={ "class":"top-players__m top-players__padded"}):
        total_match_lst.append(int(match.text.replace('\n','')))
    for ings in row.findAll('td',attrs={"class":"top-players__inns"}):
        total_inngs_lst.append(int(ings.text.replace('\n','')))
    for runs in row.findAll('td',attrs={"class":"top-players__r is-active"}):
#             print(runs.text)
            runs_lst.append(int(runs.text.replace('\n','')))
    for hs in row.findAll('td',attrs={"class":"top-players__hs"}):
        hs_lst.append(hs.text.replace('\n','')) 
    for avg in row.findAll('td',attrs={"class":"top-players__a"}):
        avg_lst.append(avg.text.replace('\n',''))
    for sr in row.findAll('td',attrs={'class':"top-players__sr"}):
        sr_lst.append(sr.text.replace('\n',''))
#     print(row)
player_info['player_name']=player_name_lst
player_info['total_matches']=total_match_lst
player_info['innings']=total_inngs_lst
player_info['runs']=runs_lst
player_info['high_score']=hs_lst
player_info['average']=avg_lst
player_info['srike_rate']=sr_lst
data=pd.DataFrame(player_info)
data.to_csv('batsman_info_ipl.csv')
    
#top-bowller records

URL1='https://www.iplt20.com/stats/2020/most-wickets'
page1 = requests.get(URL1)

soup1 = BeautifulSoup(page1.content, 'html.parser')
table1 = soup1.find('div', attrs = {'class':'js-table'})
player_info1={}
player_name_lst1=[]
total_match_lst1=[]
wkts_lst=[]
avg_lst1=[]
sr_lst1=[]
for row1 in table1.findAll('table', attrs={'table table--scroll-on-tablet top-players'}):
    for k in row1.findAll('div', attrs={'class':"top-players__player-name"}):
        player_name_lst1.append(k.a['href'].split('/')[-1])
#         print(k.a['href'].split('/')[-1])
    for match1 in row1.findAll('td',attrs={ "class":"top-players__m top-players__padded"}):
        total_match_lst1.append(int(match1.text.replace('\n','')))
    for wkts in row1.findAll('td',attrs={"class":"top-players__w is-active"}):
            wkts_lst.append(int(wkts.text.replace('\n','')))
    for avg1 in row1.findAll('td',attrs={"class":"top-players__a"}):
        avg_lst1.append(avg1.text.replace('\n',''))
    for sr1 in row1.findAll('td',attrs={'class':"top-players__sr"}):
        sr_lst1.append(sr1.text.replace('\n',''))
player_info1['player_name']=player_name_lst1
player_info1['total_matches']=total_match_lst1
player_info1['wickets']=wkts_lst
player_info1['average']=avg_lst1
player_info1['srike_rate']=sr_lst1
data1=pd.DataFrame(player_info1)
data1.to_csv('bowller_info_ipl.csv')
print(data)
print('#################################')
print(data1)