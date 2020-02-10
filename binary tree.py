class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def printtree(self):
        print(self.data)
        if(self.left!=None):
            self.left.printtree()
        if(self.right!=None):
            self.right.printtree()
    def insert(self,i):
        if(self.data):
            if(i<self.data):
                if self.left is None:
                    self.left=node(i)
                else:
                    self.left.insert(i)
            if(i>self.data):
                if self.right is None:
                    self.right=node(i)
                else:
                    self.right.insert(i)
        else:
            self.data=i
    def findval(self,val):
        
        if(self.data==val):
            print("found")
        elif(self.data>val):
            if(self.left!=None):
                self.left.findval(val)
            else:
                print("not found")
        else:
            if(self.right!=None):
                self.right.findval(val)
            else:
                print("not found")
    def delete(self,data):
        if(self.data==data):
            if(self.left==None and self.right==None):
                self.data=None
            elif(self.left==None):
                self.data=self.right.data
                self.right.delete(self.right.data)
            elif(self.right==None):
                self.data=self.left.data
                self.left.delete(self.left.data)
            else:
                self.data=self.left.data
                self.left.delete(self.left.data)
        elif(self.data<data):
            self.right.delete(data)
        else:
            self.left.delete(data)
    
        
            
            
        
            
            
        
root=node(6)
root.insert(4)
root.insert(3)
root.insert(7)
root.insert(10)
root.insert(1)
root.insert(9)

root.delete(6)
root.printtree()


        
