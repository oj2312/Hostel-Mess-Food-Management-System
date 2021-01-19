class Menu:
    def __init__(self,name,flist,fdict):
        self.name=name
        self.flist=flist
        self.fdict=fdict

    def get_mcost(self):
        self.cost=0
        for i in self.flist:
            self.cost=self.cost+self.fdict[i]
        return self.cost

    def get_foods(self):
        return self.flist




'''TESTING
def Convert(string):
    li = list(string.split(" ")) 
    return li 

f1=open("Foods.pickle","rb")
ct=[]
x=""
l=[]
d={}
while 1:
    try:
        f2=pickle.load(f1)
        x=x+f2.name
        ct.append(f2.get_cost())
        x=x+" "
    except(EOFError):
        break

l=Convert(x)
l.pop()
print(ct)
file=open("foods_costs.txt","r")
s=file.read()
d=eval(s)
file.close()

print(l)
print(d)
m1=Menu("menu1",l,d)

print(m1.name)
c=m1.get_mcost()
print(c)
WORKING'''
