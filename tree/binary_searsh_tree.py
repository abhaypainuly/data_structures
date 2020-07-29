from collection import OrderedDict

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




class Tnode():
    
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)


class Tree():
    
    def __init__(self,root=None):
        self.root = root
        
    def add(self,data):
        new_node = Tnode(data)
        if self.root is None:
            self.root = new_node
            return
        cur_root = self.root
        while True:
            if cur_root.data == data:
                print('Dublicate values not allowed in BST!')
                return
            elif cur_root.data > data:
                if cur_root.left == None:
                    cur_root.left = new_node
                    return
                cur_root = cur_root.left                
            else:
                if cur_root.right == None:
                    cur_root.right = new_node
                    return
                cur_root = cur_root.right
    
    def search(self,data):
        if self.root == None:
            print('Tree is Empty!')
            return
        cur_root = self.root
        while cur_root != None:
            if cur_root.data == data:
                return True
            elif cur_root .data > data:
                cur_root = cur_root.left
            else:
                cur_root = cur_root.right
        return False
    
    def mini(self):
        if self.root == None:
            print('Tree is Empty!')
            return
        cur_root = self.root
        while cur_root.left != None:
            cur_root = cur_root.left
            
        return cur_root.data
    
    def maxi(self):
        if self.root == None:
            print('Tree is Empty!')
            return
        cur_root = self.root
        while cur_root.right != None:
            cur_root = cur_root.right
        return cur_root.data
    
    def prt(self):
        if self.root == None:
            print('Tree is Empty!')
            return
        
        def recur(root):
            if root is None:
                return
            recur(root.left)
            print(root.data)
            recur(root.right)
        
        recur(self.root)
    
    def height(self):
        def recur(root):
            if root == None:
                return -1
            return max(recur(root.left),recur(root.right))+1
        return recur(self.root)
    
    def loTraversal(self):        
        if self.root == None:
            return
        q = Queue()
        root = self.root
        while root != None:
            print(root.data,end=' ')
            if root.left != None:
                q.push(root.left)
            if root.right != None:
                q.push(root.right)
            root = q.pop()
    
    def delete(self,data):
        if self.root == None:
            return
        def findMax(root):
            while root.right != None:
                root = root.right
            return root
        def del_recur(root,data):
            if root.data == data:
                if root.left == None and root.right == None:
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                max_root = findMax(root.left)
                root.data = max_root.data
                root.left = del_recur(root.left,max_root.data)                
            elif root.data>data:
                root.left = del_recur(root.left,data)
            else:
                root.right = del_recur(root.right,data)
            return root
        self.root = del_recur(self.root,data)
        
    def inOrderSuccessor(self,data):
        if self.root == None:
            print('Tree is Empty')
            return

        #Finding root node of the data given 
        cur_root = self.root
        while cur_root!= None:
            if data < cur_root.data:
                cur_root = cur_root.left
            elif data > cur_root.data:
                cur_root = cur_root.right
            else:
                break

        if cur_root.right != None:
            #Finding minimum in right of the current root
            temp = cur_root.right
            while temp.left != None:
                temp = temp.left
            print(temp.data)
        else:
            #Finding the depest node whose current root is in left sub tree
            successor = None
            ancestor = self.root
            while ancestor != None:
                if data < ancestor.data:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            if successor == None:
                print('No succesor!')
            else:
                print(successor.data)
    
    def leftView(self):
        if self.root == None:
            return
        lst = []
        lst.append(self.root)
        while len(lst) != 0:
            l = len(lst)
            print(lst[0],end=' ')            
            for _ in range(l):
                if lst[0].left != None:
                    lst.append(lst[0].left)
                if lst[0].right != None:
                    lst.append(lst[0].right)
                lst.pop(0)
    
    def rightView(self):
        if self.root == None:
            return
        lst = []
        lst.append(self.root)
        while len(lst) != 0:
            l = len(lst)
            print(lst[0],end=' ')            
            for _ in range(l):
                if lst[0].right != None:
                    lst.append(lst[0].right)
                if lst[0].left != None:
                    lst.append(lst[0].left)                
                lst.pop(0)
    
    def topView(self):
        if self.root == None:
            return
        lst = []
        dit = OrderedDict()
        lst.append((0,self.root))
        
        while len(lst) != 0:
            v,root = lst[0]
            if v not in dit:
                dit[v] = root.data
            if root.left != None:
                lst.append((v-1,root.left))
            if root.right != None:
                lst.append((v+1,root.right))
            lst.pop(0)
        
        for i in sorted(dit.keys()):
            print(dit[i],end=' ')
        
    def bottomView(self):
        if self.root == None:
            return
        lst = []
        dit = OrderedDict()
        lst.append((0,self.root))
        
        while len(lst) != 0:
            v,root = lst[0]
            dit[v] = root.data
            if root.left != None:
                lst.append((v-1,root.left))
            if root.right != None:
                lst.append((v+1,root.right))
            lst.pop(0)
        
        for i in sorted(dit.keys()):
            print(dit[i],end=' ')




t1 = Tree()
t1.add(5)
t1.add(2)
t1.add(3)
t1.add(8)
t1.add(10)
t1.add(1)
print(t1.search(1))
print(t1.search(10))
print(t1.search(15))
t1.prt()
t1.maxi()
t1.mini()
t1.height()

t1.inOrderSuccessor(10)
t1.loTraversal()
t1.delete(10)
print(t1.search(10))