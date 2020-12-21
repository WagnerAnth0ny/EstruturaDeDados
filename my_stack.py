import my_linked_list
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
                return (team_csv['team_short_name'][t])

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


    #Remove from stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty!")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


#This function get the data in the given position
def get(pilha, position):
    l = my_linked_list.Linked_list()
    i = 0
    while i < position:
        i += 1
        l.push(pilha.pop())
    element = pilha.pop()
    pilha.push(element)
    for x in range(l.size()).__reversed__():
        pilha.push(l.get(x))
    return element

#This function find a position of an given id
def find_position(pilha, id):
    for x in range(pilha.getSize()):
        if get(pilha, x).match_api_id == id:
            return x

#This function modify the data in the given position
def modify(pilha, new_data, id):
    position = find_position(pilha, id)
    l = my_linked_list.Linked_list()
    i = 0
    while i < position:
        i += 1
        l.push(pilha.pop())
    element = pilha.pop()
    pilha.push(new_data)
    for x in range(l.size()).__reversed__():
        pilha.push(l.get(x))