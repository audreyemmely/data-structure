import pandas as pd
csvData = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertByLikes(self, data):

        if self.data[8]:
            if data[8] < self.data[8]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByLikes(data)
            elif data[8] > self.data[8]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByLikes(data)
        else:
            self.data = data

    def insertByTitle(self, data):

        if self.data[2]:
            if data[2] < self.data[2]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByTitle(data)
            elif data[2] > self.data[2]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByTitle(data)
        else:
            self.data = data

    def insertByViews(self, data):

        if self.data[7]:
            if data[7] < self.data[7]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByViews(data)
            elif data[7] > self.data[7]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByViews(data)
        else:
            self.data = data

    def showTree(self): #Em ordem
        if self.left:
            self.left.showTree()
        print( self.data),
        print("\n")
        if self.right:
            self.right.showTree()
            

def treeMenu(csvData):    

    data = csvData.sample(100)
    root = Node(data.iloc[0])
    
    i=1
    while(i < 10):
                root.insertByViews(data.iloc[i]) 
                i+=1


    root.showTree()

treeMenu(csvData)

# Falta: Organizar menu, Funções delete
