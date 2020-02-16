#import sys
from collections import defaultdict as dd
class graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=dd(list)
        #print(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def allpaths(self,u,d,path,visited):
        #print(visited)
        visited[u]=1
        #print(visited[u])
        path.append(u)
        if(u==d):
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i]==-1:
                    self.allpaths(i,d,path,visited)
        path.pop()
        visited[u]=False
        print(path)
    def printpaths(self,s,d):
        visited=[]
        for i in range(0,self.v):
            visited.append(-1)
        #print(visited)
             
        path=[]
        self.allpaths(s,d,path,visited)
g=graph(4)
#print(g.graph)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(0,3)
g.addedge(2,0)
g.addedge(2,1)
g.addedge(1,3)
g.printpaths(2,3)
        
    
