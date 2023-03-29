class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    def display(self):
        while self.head is not None:
            print(self.head.data)
            self.head=self.head.next
    def inserting_start(self,newword):
        new=Node(newword)
        new.next = self.head
        self.head = new
    
        

list_1=Linked_list()
list_1.head= Node("hari")
second = Node("ravi")
third = Node("ramu")

list_1.head.next = second
second.next = third

list_1.inserting_start("RRR")
list_1.display()
