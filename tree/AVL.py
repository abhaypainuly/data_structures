#AVL Tree
class Node():
    def __init__(self,data, height=1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = height
        
    def _str__(self):
        return str(self.data)

class AVLtree():
    def __init__(self, root=None):
        self.root = root
        
    def getHeight(root):
        if root == None:
            return 0
        return root.height
    
    def adjustHeight(root):
        root.height = max(AVLtree.getHeight(root.left), AVLtree.getHeight(root.right)) + 1
        
    def getMax(root):
        while root.right != None:
            root = root.right
        return root.data
    
    def display(self):
        def displayHelper(root):
            if root == None:
                return
            
            displayHelper(root.left)
            print(root.data, end=' ')
            displayHelper(root.right)
        
        displayHelper(self.root)
        print()   
        
    def getBalanceFactor(root):
        if root == None:
            return 0
        
        if root.left == None:
            leftHeight = 0
        else:
            leftHeight = root.left.height
        
        if root.right == None:
            rightHeight = 0
        else:
            rightHeight = root.right.height
        
        return leftHeight - rightHeight
    
    def rightRotate(root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        AVLtree.adjustHeight(root)
        return newRoot

    def leftRotate(root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        AVLtree.adjustHeight(root)
        return newRoot 
    
    def adjustImbalance(root):
        if root==None:
            return root
        balanceFactor = AVLtree.getBalanceFactor(root)
            
        if balanceFactor>1:
            if AVLtree.getHeight(root.left.left) < AVLtree.getHeight(root.left.right):
                newRoot = root.left.right
                root.left.right = newRoot.left
                AVLtree.adjustHeight(root.left)
                newRoot.left = root.left
                root.left = newRoot
            root = AVLtree.rightRotate(root)

        if balanceFactor<-1:
            if AVLtree.getHeight(root.right.left) > AVLtree.getHeight(root.right.right):
                newRoot = root.right.left
                root.right.left = newRoot.right
                AVLtree.adjustHeight(root.right)
                newRoot.right = root.right
                root.right = newRoot
            root = AVLtree.leftRotate(root) 

        AVLtree.adjustHeight(root)
        return root
        
        
    def insert(self, data):        
        def insertHelper(root, data):
            if root == None:
                return Node(data)
            elif root.data > data:
                root.left = insertHelper(root.left, data)
            else:
                root.right = insertHelper(root.right, data)
                
            root = AVLtree.adjustImbalance(root)                     
            return root
        
        self.root = insertHelper(self.root, data)
        
        
    def remove(self,data):
        def removeHelper(root, data):
            if root == None:
                return root
            
            if data < root.data:
                root.left = removeHelper(root.left, data)
            elif data > root.data:
                root.right = removeHelper(root.ruight, data)
            else:
                if root.left == None and root.right == None:
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                else:
                    newData = AVLtree.getMax(root.left)
                    root.data = newData
                    root.left = removeHelper(root.left, data)
                    
            root = AVLtree.adjustImbalance(root)
            return root
        
        self.root = removeHelper(self.root, data)

t = AVLtree()

t.insert(1)
t.display()
print(t.root.data)
print()

t.insert(2)
t.display()
print(t.root.data)
print()

t.insert(5)
t.display()
print(t.root.data)
print()

t.insert(8)
t.display()
print(t.root.data)
print()

t.remove(1)
t.display()
print(t.root.data)
print()