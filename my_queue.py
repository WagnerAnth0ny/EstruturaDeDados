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
    #Create the node of the data structure
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:

    #This method initializes the queue
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    #Put the data in the end of the queue
    def enqueue(self, data):
        new_node = Node(data)
        prev = self.tail.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1

    #Remove the data from the head of the queue
    def dequeue(self):
        d = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return d.data

    #Get the size of the queue
    def getSize(self):
        return self.size

    #Print the queue
    def print(self):
        cur = self.head.next
        for x in range(self.size):
            print(cur)
            cur = cur.next

    #Get the data in a given position of the queue
    def get(self, position):
        i = 0
        cur = self.head.next
        while i < position:
            cur = cur.next
            i += 1
        return cur.data

    #Modify the data in a given position of the queue
    def modify(self, matchID, newData):
        i = 0
        cur = self.head.next
        while i < self.size:
            if cur.data.match_api_id == matchID:
                cur.data = newData
                break
            cur = cur.next

    #Sort the queue by the match_api_id
    def _sortMatchApiID(self, cur, size, i):
        if i < size:

            c_id = cur.data.match_api_id
            cn_id = cur.next.data.match_api_id

            if c_id > cn_id:

                cur.data, cur.next.data = cur.next.data, cur.data

            self._sortMatchApiID(cur.next, size, i + 1)

    #Sort the queue by the league_id
    def _sortLeagueID(self, cur, size, i):
        if i < size:

            c_id = cur.data.league_id
            cn_id = cur.next.data.league_id

            if c_id > cn_id:
                cur.data, cur.next.data = cur.next.data, cur.data

            self._sortLeagueID(cur.next, size, i + 1)

    #Sort the data by id
    def _sortID(self, cur, size, i):
        if i < size:

            c_id = cur.data.id
            cn_id = cur.next.data.id

            if c_id > cn_id:
                cur.data, cur.next.data = cur.next.data, cur.data

            self._sortID(cur.next, size, i + 1)

    #Select wich sort function will be used
    def sortMatch(self, parameter = None):

        if parameter == "id":
            for i in range(self.size):
                self._sortID(self.head.next, self.size - 1, 0)
        elif parameter == "league_id":
            for i in range(self.size):
                self._sortLeagueID(self.head.next, self.size - 1, 0)
        else:
            for i in range(self.size):
                self._sortMatchApiID(self.head.next, self.size - 1, 0)




