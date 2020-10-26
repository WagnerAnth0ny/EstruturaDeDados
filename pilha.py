import pandas as pd
import random

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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #This method initializes the stack
    #Initializing stack
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    #get size of stack
    def getSize(self):
        return self.size

    #check if stack is empty
    def isEmpty(self):
        return self.size == 0

    #Get the item on top of stack
    def peek(self):
        # Checking if stack is empty before getting the top item
        if self.isEmpty():
            raise Exception("Stack is empty!")
        return self.head.next.value

    #Insert a value into the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    #Get a element of the stack
    def get(self, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        return cur.value

    #Modify the value of a node
    def modify(self, new_data, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        cur.value = new_data

    #Remove from stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty!")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

def get_randoms(data):
    #This function returns an aleatory int smaller than the lenght of the dataset

    #Get the lenght of the dataset
    l = len(data['id']) - 1

    #Return an aleatory int
    return random.randint(0, l)

#Get the data of the csv and put it in a dataframe of pandas library
match = pd.read_csv('match.csv')
country = pd.read_csv('country.csv')
league = pd.read_csv('league.csv')
player = pd.read_csv('player.csv')
player_attributes = pd.read_csv('player_attributes.csv')
team = pd.read_csv('team.csv')
team_attributes = pd.read_csv('team_attributes.csv')

#Creat the stack
pilha = Stack()

#Put the data in the stack
for x in range(100):

    pilha.push(Data_match(match, get_randoms(match)))

#Print the size of of the stack
print("Tamanho da pilha: " + str(pilha.size))

#Print 100 match_id from the stack
for x in range(100):

    print(pilha.get(x).match_api_id)
