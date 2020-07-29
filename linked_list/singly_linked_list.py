class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)+' '



class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    def __str__(self):
        cur_node = self.head
        while cur_node!=None:
            print(cur_node, end='')
            cur_node = cur_node.next
        return ''
    
    def remove(self,data):
        cur_node = self.head
        prev_node = None
        while cur_node.next != None:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                prev_node.next = cur_node.next
                print('{} is removed!'.format(data))
                break
        if cur_node.next == None:
            print('NO such Element!')
        elif prev_node == None:
            print('Linked list is Empty!')
            
    def rev_print(self):
        def rev_call(head):
            if head is None:
                return
            rev_call(head.next)
            print(head,end=' ')            
        rev_call(self.head)
    
    def reverse(self):
        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node
        
    def recur_reverse(self):
        def recurse(cur_node):
            if cur_node.next is None:
                self.head = cur_node
                return
            recurse(cur_node.next)
            next_node = cur_node.next
            next_node.next = cur_node
            cur_node.next = None            
        recurse(self.head)

llist = LinkedList()
for i in range(10):
    llist.add(i)
print(llist)
llist.remove(5)
llist.remove(2)
print(llist)
llist.reverse()
print(llist)
llist.recur_reverse()
print(llist)