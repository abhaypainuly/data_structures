class Node():
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def pop(self):
        if self.head == None:
            return
        data = self.head.data
        self.head = self.head.next
        return data
        
    def ptr(self):
        if self.head == None:
            return
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data,end=' ')
            cur_node = cur_node.next
        print()