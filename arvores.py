import pandas as pd
import random
import my_tree

def get_randoms(data):
    # This function returns an aleatory int smaller than the lenght of the dataset

    # Get the lenght of the dataset
    l = len(data['id']) - 1

    # Return an aleatory int
    return random.randint(0, l)

#Get the data of the csv and put it in a dataframe of pandas library
match = pd.read_csv('match.csv')
country = pd.read_csv('country.csv')
league = pd.read_csv('league.csv')
player = pd.read_csv('player.csv')
player_attributes = pd.read_csv('player_attributes.csv')
team = pd.read_csv('team.csv')
team_attributes = pd.read_csv('team_attributes.csv')

tree = my_tree.BinaryTree()

for x in range(100):
    tree.insert(my_tree.Data_match(match,get_randoms(match)))


tree.printTree()

print(" ")

tree.modify(int(input("Digite um id: ")), my_tree.Data_match(match, get_randoms(match)))

print(" ")

tree.printTree()



