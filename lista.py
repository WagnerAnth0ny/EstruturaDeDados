import pandas as pd
import random
import my_linked_list

def get_randoms(data):
    # This function returns an aleatory int smaller than the lenght of the dataset

    # Get the lenght of the dataset
    l = len(data['id']) - 1

    # Return an aleatory int
    return random.randint(0, l)

#Get the data of the csv and put it in a dataframe of palista.pyndas library
match = pd.read_csv('match.csv')
country = pd.read_csv('country.csv')
league = pd.read_csv('league.csv')
player = pd.read_csv('player.csv')
player_attributes = pd.read_csv('player_attributes.csv')
team = pd.read_csv('team.csv')
team_attributes = pd.read_csv('team_attributes.csv')

#Create the list
lista = my_linked_list.Linked_list()

#Put the data in the list
for x in range(1060):

    lista.push(my_linked_list.Data_match(match,get_randoms(match)))

#Print 100 match_id from the list
for x in range(lista.size()):

    print(lista.get(x).match_api_id)

print(" ")

#Modify the data in the given position
#lista.modify(my_linked_list.Data_match(match,get_randoms(match)), 3)

#Print 100 match_id from the list
for x in range(lista.size()):

    print(lista.get(x).match_api_id)

print(" ")

#Print the size of the list
print("Size of the list: " + str(lista.size()))

#Delete the node with the given id
lista.pop(int(input("digite um id para excluir: ")))


#Print the size of the list
print(lista.size())




