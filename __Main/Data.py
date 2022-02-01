class Data:

    def __init__(self,x):
        self.x=x

    def __repr__(self):
        return f"{self.x}"

    def __eq__(self, other):
       
        return self.x==other.x

mylist=[]
for i in range(10):
    mylist.append( Data(i) )
    
print(mylist)

mylist.remove( mylist[3] )
print(mylist)

mylist.remove( Data(5) )
print(mylist)

