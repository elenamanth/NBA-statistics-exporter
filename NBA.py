import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from matplotlib import pyplot as plt
from nba_api.stats.endpoints import playercareerstats

from nba_api.stats import endpoints
from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
print('Number of teams: {}'.format(len(nba_teams)))
nba_teams[:2]

#BUCKS
bucks = [team for team in nba_teams
         if team['abbreviation'] == 'MIL'][0]

bucks_id = bucks['id']

from nba_api.stats.static import players
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
print('Number of players fetched: {}'.format(len(nba_players)))
nba_players[:2]

#GIANNIS
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog

Giannis = [player for player in nba_players
                   if player['full_name'] == 'Giannis Antetokounmpo'][0]
Giannis_id = Giannis['id']
Giannis
career = playercareerstats.PlayerCareerStats(player_id = Giannis_id)
#career.get_data_frames()[0]

#SEASON 2020
game_gian = playergamelog.PlayerGameLog(player_id= Giannis_id, season = '2020')
df_gian_games_2020 = game_gian.get_data_frames()[0]


game_gian_all = playergamelog.PlayerGameLog(player_id=Giannis_id, season = SeasonAll.all)
df_gian_games_all = game_gian_all.get_data_frames()[0]


PTS = df_gian_games_2020.iloc[:,24]
GAME_D = df_gian_games_2020.iloc[:,3]
MATCH = df_gian_games_2020.iloc[:,4]


for i in range(len(df_gian_games_2020)):
    if (PTS[i] == max(PTS)):
        print("Max points on season 2020: " + str(max(PTS))+ " on " + str(GAME_D[i]) + ", " + str(MATCH[i]))
        

df_gian_games_2020.plot(x ='MIN', y='PTS', kind = 'scatter')

#SEASON 2021
from numpy import mean
game_gian = playergamelog.PlayerGameLog(player_id= Giannis_id, season = '2021')
df_gian_games_2021 = game_gian.get_data_frames()[0]


game_gian_all = playergamelog.PlayerGameLog(player_id=Giannis_id, season = SeasonAll.all)
df_gian_games_all = game_gian_all.get_data_frames()[0]


PTS = df_gian_games_2021.iloc[:,24]
GAME_D = df_gian_games_2021.iloc[:,3]
MATCH = df_gian_games_2021.iloc[:,4]

mean_points=mean(PTS)
for i in range(len(df_gian_games_2021)):
    if (PTS[i] == max(PTS)):
        print("Max points on season 2021: " + str(max(PTS))+ " on " + str(GAME_D[i]) + ", " + str(MATCH[i])+ ". Mean points: "+ str(mean_points))
             
df_gian_games_2021.plot(x ='GAME_DATE', y='PTS', kind = 'scatter')

data = endpoints.leagueleaders.LeagueLeaders() 
df = data.league_leaders.get_data_frame()
 
#TOP5 scorers
max(df.loc[:,'PTS'])
df.iloc[0:5,:]

#POINTS vs MINUTES
df.plot(x ='MIN', y='PTS', kind = 'scatter')
