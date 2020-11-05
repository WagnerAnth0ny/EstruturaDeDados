import pandas as pd
import random
import my_queue

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

#Create the queue
fila = my_queue.Queue()

#Put the data in the queue
for x in range(100):
    fila.enqueue(my_queue.Data_match(match, get_randoms(match)))

#Sort the queue by the match_api_id
fila.sortMatch()

for x in range(fila.getSize()):
    print(fila.get(x).match_api_id)

print(" ")

#Print the size of the queue
print("Size of the queue: " + str(fila.getSize()))

#Remove an element of the queue
fila.dequeue()

print(" ")

#Get the size of the queue
print("Size of the queue: " + str(fila.getSize()))
