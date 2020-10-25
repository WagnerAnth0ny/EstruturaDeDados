import pandas as pd
import random

class Data_match:

    def __init__(self, data, position):
        self.id = data['id'][position]
        self.league_id = data['league_id'][position]
        self.season = data['season'][position]
        self.stage = data['stage'][position]
        self.date = data['date'][position]
        self.match_api_id = data['match_api_id'][position]
        self.home_team_api_id = data['home_team_api_id'][position]
        self.away_team_api_id = data['away_team_api_id'][position]
        self.goal = data['goal'][position]
        self.shoton = data['shoton'][position]
        self.shotoff = data['shotoff'][position]
        self.foulcommit = data['foulcommit'][position]
        self.card = data['card'][position]
        self.cross = data['cross'][position]
        self.corner = data['corner'][position]
        self.possession = data['possession'][position]

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = Node()

    def push(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def print(self):
        cur = self.head.next
        while cur.next != None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    def get(self, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        return cur.data

    def modify(self, new_data, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        cur.data = new_data

    def pop(self, position):
        i = 0
        cur = self.head.next
        prev = self.head
        while i < position:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next

def get_randoms(data):

    l = len(data['id']) - 1
    return random.randint(0, l)


match = pd.read_csv('match.csv')
country = pd.read_csv('country.csv')
league = pd.read_csv('league.csv')
player = pd.read_csv('player.csv')
player_attributes = pd.read_csv('player_attributes.csv')
team = pd.read_csv('team.csv')
team_attributes = pd.read_csv('team_attributes.csv')

lista = Linked_list()

for x in range(100):

    lista.push(Data_match(match,get_randoms(match)))

for x in range(100):

    print(lista.get(x).match_api_id)





