import pandas as pd
import random
import my_graph

def get_randoms(data):
    #This function returns an aleatory int smaller than the lenght of the dataset

    #Get the lenght of the dataset
    l = len(data['_unit_id']) - 1

    #Return an aleatory int
    return random.randint(0, l)

#Get the data of the csv and put it in a dataframe of pandas library
data = pd.read_csv('gender-classifier-DFE-791531.csv', encoding='latin1')

#Create the graph
graph = my_graph.Graph()

#Put the data in the graph
for x in range(100):
    graph.add(my_graph.Profile_data(data, get_randoms(data)))

#Print the nodes of the graph
graph.print()

#Print the shortest path between two nodes
graph.short_path(int(input("Digite o primeiro no: ")), int(input("Digite o segundo no: ")))

