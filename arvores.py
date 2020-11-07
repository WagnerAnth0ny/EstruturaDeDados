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

#Create the tree
tree = my_tree.BinaryTree()

#Put the data in the tree
for x in range(100):
    tree.insert(my_tree.Data_match(match,get_randoms(match)))

#Print the tree using match_api_id as parameter
tree.printTree()

print(" ")

#Modify one node in the tree
tree.modify(int(input("Digite um id: ")), my_tree.Data_match(match, get_randoms(match)))

print(" ")

#Print the tree using match_api_id as parameter
tree.printTree()

#Sort the tree by id
tree.sortTree("id")

print(" ")

#Print the tree using the id as parameter
tree.printTree("id")

print(" ")

#Print the tree using match_api_id as parameter
tree.printTree()



