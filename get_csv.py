import sqlite3 as sql
import pandas as pd

connection = sql.connect('database.sqlite')

match = pd.read_sql('SELECT * FROM Match', connection)

match.to_csv('match.csv')

country = pd.read_sql('SELECT * FROM Country', connection)

country.to_csv('country.csv')

league = pd.read_sql('SELECT * FROM League', connection)

league.to_csv('league.csv')

player = pd.read_sql('SELECT * FROM Player', connection)

player.to_csv('player.csv')

player_attributes = pd.read_sql('SELECT * FROM Player_Attributes', connection)

player_attributes.to_csv('player_attributes.csv')

team = pd.read_sql('SELECT * FROM Team', connection)

team.to_csv('team.csv')

team_attributes = pd.read_sql('SELECT * FROM Team_Attributes', connection)

team_attributes.to_csv('team_attributes.csv')