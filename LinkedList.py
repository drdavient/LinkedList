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
         self.head=self.head.next
         return temp
         
     
         
class Node:

    def __init__(self, name):
        self.name = name
        self.next =None
        
    
    

if (__name__=="__main__"):
    print("hello")
    node1 =Node('A')
    print (node1.name)
    letterList = LinkedList ("Letter List")
    for char in string.ascii_lowercase:
        letterList.Push(Node(char))
    
    current = letterList.head
    alphabet=""
    reverse=""
    while (current!=None):
        alphabet +=current.name        
        current=current.next
        
    print(alphabet)
    reverse =""
    while(letterList.head):
         reverse=letterList.Pop().name+reverse
         
    print(reverse)
    
        
    