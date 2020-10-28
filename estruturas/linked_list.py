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
            print("\n")
            aux = aux.nextNode
    
    def delete(self, video_id):
        #nodeValue[0] retorna o valor do video_id do item da lista
        if(self.head.nodeValue[0].lower() == video_id.lower()):
            self.head = self.head.nextNode
            return video_id +" foi deletado.\n"
        else:
            aux = self.head
            previous = None
            while (aux.nextNode != None):
                previous = aux
                aux = aux.nextNode
                if(aux.nodeValue[0].lower() == video_id.lower() and aux.nextNode != None):
                    previous.nextNode = aux.nextNode
                    return video_id +" foi deletado.\n"
                elif(aux.nodeValue[0].lower() == video_id.lower() and aux.nextNode == None):
                    previous.nextNode = None
                    return video_id +" foi deletado.\n"
            return video_id +" não está na lista.\n"

