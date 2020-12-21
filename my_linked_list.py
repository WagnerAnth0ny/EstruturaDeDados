import pandas as pd

class Data_match:

    #This method saves the data from the dataframe

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
        self.away_team_name = self.findName(self.away_team_api_id)
        self.home_team_name = self.findName(self.home_team_api_id)

    def findName(self, id):
        team_csv = pd.read_csv('team.csv')

        l = len(team_csv['id']) - 1

        for t in range(l):
            if team_csv['team_api_id'][t] == id:
                return(team_csv['team_short_name'][t])

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:

    # This method initializes the list
    # Initializing list
    def __init__(self):
        self.head = Node()

    #Get the size of the list
    def size(self):
        i = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            i += 1
        return i

    #Put a new element in the list
    def push(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    #Print the list
    def print(self):
        cur = self.head.next
        while cur.next != None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    #Get a element of the list
    def get(self, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        return cur.data

    #Find the position of a given id
    def findPosition(self, id):
        i = 0
        while i < self.size():
            if self.get(i).match_api_id == id:
                break
            i += 1
        return i

    # Mofify a element of the list
    def modify(self, new_data, id):

        i = 0
        cur = self.head.next
        while i < self.findPosition(id) + 1:
            cur = cur.next
            i += 1
        cur.data = new_data

    # Remove a element of the list
    def pop(self, id):
        i = 0
        cur = self.head.next
        prev = self.head
        while i < self.findPosition(id) + 1:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next

        return cur.data



