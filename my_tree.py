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
    def __init__(self, data = None):
        self.parent = None
        self.right = None
        self.left = None
        self.data = data

class BinaryTree:

    # This method initializes the tree
    # Initializing the tree
    def __init__(self):
        self.root = Node()

    #Insert a new node in the tree using match_api_id as parameter
    def _insertMatchID(self, newData, cur):
        if newData.match_api_id >= cur.data.match_api_id:
            if cur.right == None:
                cur.right = Node(newData)
                cur.right.parent = cur
            else:
                self._insertMatchID(newData, cur.right)
        else:
            if cur.left == None:
                cur.left = Node(newData)
                cur.left.parent = cur
            else:
                self._insertMatchID(newData, cur.left)

    #Insert a new node in the tree using id as parameter
    def _insertID(self, newData, cur):
        if newData.id >= cur.data.id:
            if cur.right == None:
                cur.right = Node(newData)
                cur.right.parent = cur
            else:
                self._insertID(newData, cur.right)
        else:
            if cur.left == None:
                cur.left = Node(newData)
                cur.left.parent = cur
            else:
                self._insertID(newData, cur.left)

    #Insert a new node in the tree using league_id as parameter
    def _insertLeagueID(self, newData, cur):
        if newData.league_id >= cur.data.league_id:
            if cur.right == None:
                cur.right = Node(newData)
                cur.right.parent = cur
            else:
                self._insertLeagueID(newData, cur.right)
        else:
            if cur.left == None:
                cur.left = Node(newData)
                cur.left.parent = cur
            else:
                self._insertLeagueID(newData, cur.left)

    #Insert a new node in the tree
    def insert(self, newData, parameter = "match_api_id"):
        if self.root.data == None:
            self.root.data = newData
        else:
            if parameter == "id":
                self._insertID(newData, self.root)
            elif parameter == "league_id":
                self._insertLeagueID(newData, self.root)
            else:
                self._insertMatchID(newData, self.root)

    #Print the tree using match_api_id as parameter
    def _printTreeMatchID(self, cur):
        if cur != None:
            self._printTreeMatchID(cur.left)
            print(cur.data.match_api_id)
            self._printTreeMatchID(cur.right)

    #Print the tree using id as parameter
    def _printTreeID(self, cur):
        if cur != None:
            self._printTreeID(cur.left)
            print(cur.data.id)
            self._printTreeID(cur.right)

    #Print the tree using league_id as parameter
    def _printTreeLeagueID(self, cur):
        if cur != None:
            self._printTreeLeagueID(cur.left)
            print(cur.data.league_id)
            self._printTreeLeagueID(cur.right)

    #This method print the tree
    def printTree(self, parameter = "match_api_id"):
        if self.root != None:
            if parameter == "id":
                self._printTreeID(self.root)
            elif parameter == "league_id":
                self._printTreeLeagueID(self.root)
            else:
                self._printTreeMatchID(self.root)

    #Get the tree data by the match_api_id
    def _getSubTreeMatchID(self, cur, matchID = None):
        if cur != None:
            self._getSubTreeMatchID(cur.left, matchID)
            if cur.data.match_api_id != matchID:
                self.insert(cur.data)
            self._getSubTreeMatchID(cur.right, matchID)

    # Delete a node using the match_api_id as parameter
    def _deleteMatchID(self, cur, matchID, prev = None):
        if cur != None:
            if cur.data.match_api_id == matchID:
                save = cur
                if prev.right != None:
                    if prev.right.data.match_api_id == matchID:
                        prev.right = None
                if prev.left != None:
                    if prev.left.data.match_api_id == matchID:
                        prev.left = None
                self._getSubTreeMatchID(save, matchID)
            self._deleteMatchID(cur.left, matchID, cur)
            self._deleteMatchID(cur.right, matchID, cur)

    # Get the tree data by the id
    def _getSubTreeID(self, cur, id = None):
        if cur != None:
            self._getSubTreeID(cur.left, id)
            if cur.data.id != id:
                self.insert(cur.data, "id")
            self._getSubTreeID(cur.right, id)

    # Delete a node using the id as parameter
    def _deleteID(self, cur, id, prev = None):
        if cur != None:
            if cur.data.id == id:
                save = cur
                if prev.right != None:
                    if prev.right.id == id:
                        prev.right = None
                if prev.left != None:
                    if prev.left.id == id:
                        prev.left = None
                self._getSubTreeID(save, id)
            self._deleteID(cur.left, id, cur)
            self._deleteID(cur.right, id, cur)

    #Get the tree data by the league_id
    def _getSubTreeLeagueID(self, cur, leagueID = None):
        if cur != None:
            self._getSubTreeLeagueID(cur.left, leagueID)
            if cur.data.league_id != leagueID:
                self.insert(cur.data, "league_id")
            self._getSubTreeLeagueID(cur.right, leagueID)

    #Delete a node using the league_id as parameter
    def _deleteLeagueID(self, cur, leagueID, prev = None):
        if cur != None:
            if cur.data.league_id == leagueID:
                save = cur
                if prev.right != None:
                    if prev.right.data.league_id == leagueID:
                        prev.right = None
                if prev.left != None:
                    if prev.left.data.league_id == leagueID:
                        prev.left = None
                self._getSubTreeLeagueID(save, leagueID)
            self._deleteLeagueID(cur.left, leagueID, cur)
            self._deleteLeagueID(cur.right, leagueID, cur)

    #Delete a node from the tree
    def delete(self, id, parameter = "match_api_id"):
        if self.root != None:
            if parameter == "id":
                self._deleteID(self.root, id)
            elif parameter == "league_id":
                self._deleteLeagueID(self.root, id)
            else:
                self._deleteMatchID(self.root, id)

    #Get the data in the modified node
    def _modifyGetSubTree(self, cur, id, newData):
        if cur != None:
            self._modifyGetSubTree(cur.left, id, newData)
            if cur.data.match_api_id != id:
                self.insert(cur.data)
            else:
                self.insert(newData)
            self._modifyGetSubTree(cur.right, id, newData)

    #This method find the node and modify its information
    def _modify(self, cur, id, newData, prev = None):
        if cur != None:
            if cur.data.match_api_id == id:
                save = cur
                if prev.right != None:
                    if prev.right.data.match_api_id == id:
                        prev.right = None
                if prev.left != None:
                    if prev.left.data.match_api_id == id:
                        prev.left = None
                self._modifyGetSubTree(save, id, newData)
            self._modify(cur.left, id, newData, cur)
            self._modify(cur.right, id, newData, cur)

    #This method modify the node data
    def modify(self, matchID, newData):
        if self.root != None:
            self._modify(self.root, matchID, newData)

    #This method sort the tree using as parameter match_api_id, league_id or id
    def sortTree(self, parameter):
        if self.root != None:
            right_node = self.root.right
            left_node = self.root.left
            self.root.right = None
            self.root.left = None
            if parameter == "match_api_id":
                self._getSubTreeMatchID(right_node)
                self._getSubTreeMatchID(left_node)
            elif parameter == "league_id":
                self._getSubTreeLeagueID(right_node)
                self._getSubTreeLeagueID(left_node)
            else:
                self._getSubTreeID(right_node)
                self._getSubTreeID(left_node)







