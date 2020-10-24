class Node:

    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.nextNode = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    
    def insertAtBeginning(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.nextNode = self.head
        self.head = newNode

    def showList(self):
        aux = self.head
        while aux != None:
            print(aux.nodeValue)
            aux = aux.nextNode
    
    # Pode ser melhor deletar o dado pelo video_id e não pelo titulo
    def delete(self, title):
        # Melhorar isso aqui, bagunça do carai
        if(self.head.nodeValue.title.lower() == title.lower()):
            self.head = self.head.nextNode
            return title +" foi deletado.\n"
        else:
            aux = self.head
            previous = None
            while (aux.nextNode != None):
                previous = aux
                aux = aux.nextNode
                if(aux.nodeValue.title.lower() == title.lower() and aux.nextNode != None):
                    previous.nextNode = aux.nextNode
                    return title +" foi deletado.\n"
                elif(aux.nodeValue.title.lower() == title.lower() and aux.nextNode == None):
                    previous.nextNode = None
                    return title +" foi deletado.\n"
            return title +" não está na lista.\n"
