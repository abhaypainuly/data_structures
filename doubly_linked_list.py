class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
    
    def add(self,data):
        if self.head == None:
            new_node = Dnode(data = data)
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        new_node = Dnode(cur_node,data)
        cur_node.next = new_node
            
    def __str__(self):
        if self.head == None:
            return ''
        cur_node = self.head
        while cur_node != None:
            print(cur_node,end = '  ')
            cur_node = cur_node.next
        return '\n'
    
    def remove(self, data = None, index = None):
        if data == None and index == None:
            print('Desired argument is not passed!')
        elif index == None:
            if self.head == None:
                print('List is Empty!')
                return
            cur_node = self.head
            while cur_node != None:
                if cur_node.data == data:
                    prev_node = cur_node.prev
                    if prev_node == None:
                        self.head = cur_node.next
                    else:                        
                        prev_node.next = cur_node.next
                    if cur_node.next is not None:
                        cur_node = cur_node.next
                        cur_node.prev = prev_node                        
                    return
                cur_node = cur_node.next
            print('Element {} is not in the list!'.format(data)) 


dllist = DoublyLinkedList()

for i in range(10):
    dllist.add(i)
print(dllist)

dllist.remove(5)
print(dllist)