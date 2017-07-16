def generateBoard():
    from random import shuffle
    x=[i for i in range(9)]
    shuffle(x)
    p=x.index(0)
    b=[]
    b.append(x[:3])
    b.append(x[3:6])
    b.append(x[6:])
    board={"i":p//3,"j":p%3,"b":b}
    return b
def printMenu():
        print("To go up, press (w),to go down press (s), to go left '\n',press (a),to go right,press (d)")

'''def clearScreen():
    import os
    clear=lamba:os.system("cls")
    clear()'''
def find0():
    pass
def moveLeft(board):
    '''
    Muta 0-ul in stanga in board
    Date de intrare:
    b- board-ul
    DAte de iesire:
    b'-board-ul modificat cu 0 mutat la stanga
    '''
    if board['j']==0:
        raise ValeError("Nu se poate muta la stanga")
    board['j']-=1
    aux=board['b'][board['i']][board['j']]
    board['b'][board['i']][board['j']]=0
    board['b'][board['i']][board['j']+1]=aux
    print(board
    print(aux)
def testmoveLeft():
    board=["i":1,"j":1,"b":[[1,2,3],[4,0,5],[6,7,8]]}
    boardnou=moveLeft(board)
    assert (boardNou["i"]==0 and boardNou['j']==1 and boardNou['b'][1][0]==
                                                                    
def printBoard(board):
    s=""
    s+=str(board["i"])+" "+str(board["j"])+'\n'
    for i in board["b"]:
        for x in i:
            if x==0:
                s+="x "
            else:
                s+=str(x)+" "
        s+='\n'
    print(s)
            
def runTests():
    pass
def run():
    printMenu()
    printBoard(generateBoard())
    
def main():
    runTests()
    run()
main()
