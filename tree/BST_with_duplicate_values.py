#Binary Tree with duplicate values

class Tnode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.count = 1
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)

class Tree():
    def __init__(self,root=None):
        self.root = root
        
    def add(self, data):
        if self.root == None:
            self.root = Tnode(data)
            return
        
        cur_node = self.root
        while True:
            if cur_node.data == data:
                cur_node.count += 1
                return
            elif data < cur_node.data:
                if cur_node.left == None:
                    cur_node.left = Tnode(data)
                    return
                cur_node = cur_node.left
            else:
                if cur_node.right == None:
                    cur_node.right = Tnode(data)
                    return
                cur_node = cur_node.right
                
    def display(self):
        def display_helper(root):
            if root == None:
                return

            display_helper(root.left)

            for i in range(root.count):
                print(root.data, end=' ')                

            display_helper(root.right)


        if self.root ==None:
            print('Tree is empty!')
            return

        display_helper(self.root)
        print()
        
    def getArr(self):
        def getArr(root, arr):
            if root==None:
                return            
            getArr(root.left, arr)            
            for i in range(root.count):
                arr.append(root.data)                
            getArr(root.right, arr)
            
        if self.root==None:
            return []
        
        arr = []
        getArr(self.root, arr)
        return arr    
    
    def delete(self,data):
        if self.root == None:
            raise Exception('Tree is empty!')
        
        def findMax(root):
            while root.right!=None:
                root = root.right
            return root 
                
        def deleteHelper(root,data):
            if root==None:
                raise Exception('Element not in Tree!')
            if root.data==data:
                if root.count>1:
                    root.count -= 1
                else:
                    if root.left==None and root.right==None:
                        return None
                    elif root.left==None:
                        return root.right
                    elif root.right == None:
                        return root.left
                    else:
                        max_root = findMax(root.left)
                        root.data= max_root.data
                        root.count = max_root.count
                        root.left = deleteHelper(root.left, max_root.data)                        
            elif data<root.data:
                root.left = deleteHelper(root.left, data)
            else:
                root.right = deleteHelper(root.right, data)                
            return root
        
        self.root = deleteHelper(self.root, data)
            
    def getMedian(self,d):
        if self.root == None:
            raise Exception('Tree is Empty!')
            
        def getMedianOdd(root, d, cf):
            if root == None:
                return
            if cf[0]>(d+1)//2:
                return            
            getMedianOdd(root.left, d, cf)
            if cf[0]<(d+1)//2:
                cf[0] += root.count
                if cf[0]>=(d+1)//2:
                    cf.append(root.data)
                    return
            getMedianOdd(root.right, d, cf)        
                
        
        def getMedianEven(root, d, cf):
            if root==None:
                return
            if cf[0]>d//2+1:
                return 
            getMedianEven(root.left, d, cf)
            if cf[0]<=d//2:
                cf[0] += root.count
                if cf[0]==d//2:
                    cf[1] = root.data
                elif cf[0]>d//2:
                    if cf[1]==None:
                        cf[1] = root.data
                        cf.append(root.data)
                    else:
                        cf.append(root.data)
                    return
            getMedianEven(root.right, d, cf)          
            
        cf = [0]
        if d%2==0:
            cf.append(None)
            getMedianEven(self.root, d, cf)
            return (cf[1]+cf[2])/2
        getMedianOdd(self.root, d, cf)
        return cf[1]


bt = Tree()
bt.add(2)
bt.add(3)
bt.add(1)
bt.add(4)
bt.add(115)
bt.add(43)
bt.add(243)
bt.add(3143)
bt.add(115)
bt.add(43)
bt.add(243)
bt.add(3143)
bt.display()

bt.getMedian(12)

