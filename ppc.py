from ctypes import cdll

import os

strs="huens %s ddd %d sdfsss"%("hello",656)
class gsc:
    def __init__(self,name,count):
        self.name=name;
        self.count=count;
    def printS(self):
        print("name %s ,count %d"%(self.name,self.count));
    def setCount(self,c):
        self.count=c;

class alt:
    def __init__(self):
        self.name="al";
        self.count=1;
    def printS(self):
        print("name %s ,count %d"%(self.name,self.count));
    def setGsc(self,c):
        ad=c
        ad.setCount(100)
        print("Y")
        
gs=gsc("hhun",9)
gs.printS();
al=alt()
al.setGsc(gs)
gs.printS();
p=os.getcwd()
print(p)
print(strs)
