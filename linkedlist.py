class linked:
    def __init__(self,data):
        self.data=data
        self.next=None
    def addend(self,data):
        if(self.next==None):
            self.next=linked(data)
        else:
            (self.next).addend(data)
    def addfront(self,data):
        temp=linked(self.data)
        temp.next=self.next
        self=linked(data)
        self.next=temp
        
        return self
    def getlength(self):
        count=0
        a=self
        while(a.next!=None):
            count=count+1
            a=a.next
        return count+1
    def deletenode(self,data):
        
        if(self.data==data):
            self=self.next
            return self
        else:
            temp=self
            while(temp.data!=data):
                self=temp
                temp=temp.next
            self.next=temp.next
            temp.next=None
    def sort(self):
        p=self
        for i in range(0,self.getlength()):
            temp=p
            for j in range(i+1,self.getlength()):
                temp=temp.next
                if(p.data<temp.data):
                    #print("k")
                    k=p.data
                    p.data=temp.data
                    temp.data=k
            p=p.next
        
                
            
                
                
                
                
                
        
            
        
        
        
        
        
    def printlist(self):
        print(self.data)
        if(self.next==None):
            return
        else:
            (self.next).printlist()
a=linked(2)
#print(a)
a.addend(5)
a.addend(7)
#a.printlist()
a=a.addfront(9)
a=a.addfront(90)
#a.printlist()
a.sort()
a.printlist()
#print(a.getlength())
            
        
        
