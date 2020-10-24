import csv

with open('dados/USvideos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader.__next__()

    for row in csv_reader:
        print( row[0] + ', ' 
        + row[1] + ', '
        + row[2] + ', '
        + row[3] + ', '
        + row[4] + ', '
        + row[5] + ', ' 
        + row[6] + ', '
        + row[7] + ', '
        + row[8] + ', '
        + row[9] + ', '
        + row[10] + ', '
        + row[11] + ', '
        + row[12] + ', '
        + row[13] + ', '
        + row[14] + ','
        + row[15])
        print('\n')

class Node: #CRIAR NÓ
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

# Function to add node
    def Atbegining(self, data_in): 
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

#Function to print node
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

#llist = SLinkedList()
#llist.Atbegining("Mon")
#llist.Atbegining("Tue")
#llist.Atbegining("Wed")
#llist.Atbegining("Thu")
#llist.RemoveNode("Tue")
#llist.LListprint()


