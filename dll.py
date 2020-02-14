class dll:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    def addnode(self,data):
        
            temp=dll(data)
            if(self.next==None):
                self.next=temp
                temp.prev=self
            else:
                while(self.next!=None):
                    self=self.next
                self.next=temp
                temp.prev=self
    def printnext(self):
        while(self.next!=None):
            print(self.data)
            self=self.next
        print(self.data)
    def printback(self):
         while(self.next!=None):
             self=self.next
         while(self.prev!=None):
             print(self.data)
             self=self.prev
         print(self.data)
        
                
a=dll(12)
a.addnode(3)
a.addnode(7)
a.printnext()
print("R")
a.printback()

        
