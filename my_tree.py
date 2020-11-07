import my_linked_list

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
    def __init__(self, data = None):
        self.parent = None
        self.right = None
        self.left = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = Node()

    def _insert(self, newData, cur):
        if newData.match_api_id >= cur.data.match_api_id:
            if cur.right == None:
                cur.right = Node(newData)
                cur.right.parent = cur
            else:
                self._insert(newData, cur.right)
        else:
            if cur.left == None:
                cur.left = Node(newData)
                cur.left.parent = cur
            else:
                self._insert(newData, cur.left)

    def insert(self, newData):

        if self.root.data == None:
            self.root.data = newData
        else:
            self._insert(newData, self.root)

    def _printTree(self, cur):
        if cur != None:
            self._printTree(cur.left)
            print(cur.data.match_api_id)
            self._printTree(cur.right)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _minimum(self, cur):
        if cur.left != None:
            self._minimum(cur.left)
        else:
            print(cur.data.match_api_id)

    def minimum(self):
        if self.root != None:
            self._minimum(self.root)


    def _maximum(self, cur):
        if cur.right != None:
            self._maximum(cur.right)
        else:
            print(cur.data.match_api_id)

    def maximum(self):
        if self.root != None:
            self._maximum(self.root)

    def _search(self, cur, id):
        if cur != None:
            if cur.data.match_api_id == id:
                return cur.data
            self._printTree(cur.left)
            self._printTree(cur.right)

    def search(self, id):
        if self.root != None:
            return self._search(self.root, id)

    def _getSubTree(self, cur, id):
        if cur != None:
            self._getSubTree(cur.left, id)
            if cur.data.match_api_id != id:
                self.insert(cur.data)
                print("inserted the data with the match_api_id: " + str(cur.data.match_api_id))
            else:
                print("not inserted the data with the match_api_id: " + str(cur.data.match_api_id))
            self._getSubTree(cur.right, id)

    def _delete(self, cur, id, prev = None):
        if cur != None:

            if cur.data.match_api_id == id:

                print("found the id node")

                save = cur

                print(save)

                if prev.right != None:
                    if prev.right.data.match_api_id == id:
                        prev.right = None
                        print("Deleted the connection in the right node")
                if prev.left != None:
                    if prev.left.data.match_api_id == id:
                        prev.left = None
                        print("Deleted the connection in the left node")

                print(save.data.match_api_id)

                self._getSubTree(save, id)

            self._delete(cur.left, id, cur)
            self._delete(cur.right, id, cur)

    def delete(self, id):
        if self.root != None:
            self._delete(self.root, id)

    def _modifyGetSubTree(self, cur, id, newData):
        if cur != None:
            self._modifyGetSubTree(cur.left, id, newData)
            if cur.data.match_api_id != id:
                self.insert(cur.data)
            else:
                self.insert(newData)
            self._modifyGetSubTree(cur.right, id, newData)

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

    def modify(self, matchID, newData):
        if self.root != None:
            self._modify(self.root, matchID, newData)








