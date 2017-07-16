def undo():
    l=[]
    l1=[]
    for i in range(4):
        l.append(i)
        l1.append(list(l))
        print(l1)
def undo1():
    l=[]
    l1=[]
    for i in range(4):
        l.append(i)
        l1.append(l)
        print(l1)
undo()
undo1()
    
