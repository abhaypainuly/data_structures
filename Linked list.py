#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)+' '


# In[3]:


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
          


# In[4]:


llist = LinkedList()


# In[5]:


for i in range(10):
    llist.add(i)
print(llist)
llist.remove(5)
llist.remove(2)
print(llist)


# In[6]:


llist.rev_print()


# In[7]:


llist.reverse()
print(llist)


# In[8]:


llist.recur_reverse()
print(llist)


# In[ ]:





# In[9]:


class Dnode():
    
    def __init__(self, prev=None, data=None, next = None):
        self.data = data
        self.next = None
        self.prev = prev
    
    def __str__(self):
        return str(self.data)


# In[10]:


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
            
        else:
            pass 


# In[11]:


dllist = DoublyLinkedList()


# In[12]:


for i in range(10):
    dllist.add(i)
print(dllist)


# In[13]:


dllist.remove(5)
print(dllist)


# In[ ]:





# In[14]:


def deleteNode(head,data):
        if head is None:
            print('List is Empty')
        if head.data == data:
            head.data = head.next.data
            head.next = head.next.next
            return
        else:
            prev_node = head
            head = head.next
            while head != None:
                if head.data == data:
                    prev_node.next = head.next
                    return
                prev_node = head
                head = head.next
            if head == None:
                print('Element not found!')


# In[15]:


llist = LinkedList()


# In[16]:


for i in range(10):
    llist.add(i)
print(llist)


# In[17]:


deleteNode(llist.head,5)
print(llist)


# In[18]:


deleteNode(llist.head,0)
print(llist)


# In[ ]:





# In[19]:


def compareLinkedLists(head1,head2):
    if head1 is None or head2 is None:
        print('Please pass non empty lists!')
        return
    while head1 != None and head2 != None:
        if head1.data > head2.data:
            return 1
        elif head1.data < head2.data:
            return -1
        else:
            head1 = head1.next
            head2 = head2.next
    if head1 is None and head2 is None:
        return 0
    elif head1 is None:
        return -1
    else:
        return 1


# In[20]:


llist1 = LinkedList()
llist1.add('g')
llist1.add('e')
llist1.add('e')
llist1.add('k')
llist1.add('s')
llist1.add('a')

llist2 = LinkedList()
llist2.add('g')
llist2.add('e')
llist2.add('e')
llist2.add('k')
llist2.add('s')
#llist2.add('b')

compareLinkedLists(llist1.head,llist2.head)


# In[21]:


#Add two number represented as linked lists
def add(head1,head2):
    if head1 == None and head2 == None:
        return Node(0)
    head = add(head1.next,head2.next)
    new_node = Node((head1.data+head2.data+head.data)%10)
    head.data = (head1.data+head2.data+head.data)//10
    new_node.next = head
    return new_node
    
def addLinkedList(head1,head2):
    cur1_node = head1
    cur2_node = head2
    l1 = 0
    l2 = 0
    
    while cur1_node!=None:
        l1 += 1
        cur_node = cur_node.next
        
    while cur2_node!=None:
        l2 += 1
        cur2_node = cur2_node.next
        
    if l1>l2:
        cur1_node = head1
        for i in range(l1-l2):
            cur1_node = cur1_node.next
        head = add(cur1_node,head2)
        
    elif l2>l1:
        cur2_node = head2
        for i in range(l2-l1):
            cur2_node = cur2_node.next
        head = add(head1,cur2_node)
        
            

