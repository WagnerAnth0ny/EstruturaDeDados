import math
from collections import defaultdict

#This function find the shortest distance between two vectors
def get_distance(vector1, vector2):

    dist = 0

    for x in range(len(vector1)):

        dist += (vector1[x] - vector2[x]) * (vector1[x] - vector2[x])

    return math.sqrt(dist)

class Profile_data:

    # This method saves the data from the dataframe
    def __init__(self, data, position):
        self.unit_id = data['_unit_id'][position]
        self.golden = data['_golden'][position]
        self.unit_state = data['_unit_state'][position]
        self.trusted_judgments = data['_trusted_judgments'][position]
        self.last_judgment_at = data['_last_judgment_at'][position]
        self.gender = data['gender'][position]
        self.gender_confidence = data['gender:confidence'][position]
        self.description = data['description'][position]
        self.fav_number = data['fav_number'][position]
        self.gender_gold = data['gender_gold'][position]
        self.link_color = data['link_color'][position]
        self.name = data['name'][position]
        self.profile_yn_gold = data['profile_yn_gold'][position]
        self.profileimage = data['profileimage'][position]
        self.retweet_count = data['retweet_count'][position]
        self.sidebar_color = data['sidebar_color'][position]
        self.text = data['text'][position]
        self.tweet_coord = data['tweet_coord'][position]
        self.tweet_count = data['tweet_count'][position]
        self.tweet_created = data['tweet_created'][position]
        self.tweet_id = data['tweet_id'][position]
        self.tweet_location = data['tweet_location'][position]
        self.user_timezone = data['user_timezone'][position]
        self.vector = self.get_vector()

    #This method create a vector for the data
    def get_vector(self):
        list = []
        list.append(self.gender_confidence)
        list.append(self.fav_number)
        list.append(self.retweet_count)
        list.append(self.tweet_count)
        return list

class Graph:

    #This method initializes the queue
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = []

    #This method adds a new node in the graph
    def add(self, new_node):

        if len(self.nodes) == 0:
            self.nodes.append(new_node)

        else:
            minor = self.nodes[0]
            minor_d = get_distance(new_node.vector, minor.vector)
            for n in self.nodes:
                if get_distance(n.vector, new_node.vector) < minor_d:
                    minor = n
                    minor_d = get_distance(n.vector, new_node.vector)

            self.graph[minor].append(new_node)
            self.graph[new_node].append(minor)
            self.nodes.append(new_node)

    #This method finds a node by a given id
    def get_node(self, id):
        for n in self.nodes:
            if n.unit_id == id:
                return n

    #This method finds the shortest path between two nodes
    def short_path(self, first_node, final_node):

        src = self.get_node(first_node)
        dest = self.get_node(final_node)
        path = []
        map = self.graph
        black_list = []

        cur = src
        prev = None
        prevv = prev

        for n in range(200):

            minor = None
            minor_d = 99999999999999999999999999

            if cur == dest:
                break

            elif map[cur] != []:
                for x in map[cur]:
                    if x not in path:
                        if get_distance(x.vector, dest.vector) < minor_d:
                            minor = x
                            minor_d = get_distance(x.vector, dest.vector)

                path.append(cur)
                prevv = prev
                prev = cur
                cur = minor

            else:
                if cur != src:
                    black_list.append(prev)
                    map[prevv].remove(prev)
                    cur = src
                    path = []
                else:
                    break

        path.append(self.get_node(final_node))

        print("Distancia: ", end=" ")
        print(len(path))
        print(" ")
        print("Caminho:")

        for n in path:
            print(n.unit_id)

    #Thus method print the nodes of the graph
    def print(self):
        print("Numero de nos:", end=" ")
        print(len(self.nodes))
        print(" ")
        for n in self.nodes:
            print(n.unit_id)



