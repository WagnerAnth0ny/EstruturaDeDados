import pandas as pd
import random
import my_stack

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
pilha = my_stack.Stack()

#Put the data in the stack
for x in range(100):

    pilha.push(my_stack.Data_match(match, get_randoms(match)))

#Print 100 match_id from the stack
for x in range(pilha.getSize()):

    print(my_stack.get(pilha, x).match_api_id)

print(" ")

#Modify the data in the given position
my_stack.modify(pilha,my_stack.Data_match(match, get_randoms(match)),3)

#Print 100 match_id from the stack
for x in range(pilha.getSize()):

    print(my_stack.get(pilha, x).match_api_id)

print(" ")

#Print the size of the stack
print("Size of the stack: " + str(pilha.getSize()))


