import string


class LinkedList:
    def __init__(self, name):
        self.head =None
        self.tail = None

    def EnQueue(self, node):
        if (self.head == None):
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def Push(self, node):
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def Pop(self):
        temp=self.head
        self.head=temp.next
        return temp

    def Reverse(self):
        self.PopTilEmpty()

    def PopTilEmpty(self):
        if(self.head):
            current = self.Pop()
            print(current.name + "Popped")
            self.PopTilEmpty();
            self.EnQueue(current);
            print(current.name + "Queued")





    def Print(self):
        alphabet=""
        current = self.head
        while (current!=None):
            alphabet += current.name
            print(alphabet)
            current=current.next
            if (current):
                alphabet += ","
        print(alphabet)



class Node:
    def __init__(self, name):
        self.name = name
        self.next = None



if (__name__=="__main__"):
    letterList = LinkedList ("Letter List")
    for char in string.ascii_lowercase:
        letterList.EnQueue(Node(char))


letterList.Reverse()
letterList.Print()
