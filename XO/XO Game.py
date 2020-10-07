####A XO Game#############
import random
pg = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def printg():
    for i in  range(3):
        st = ''
        for j in range(3):
            st += (pg[i][j]+' ')
        print(st + '\n')

def put(p,i,j):
    if p == 'x' or p== 'X':
        pg[i][j] = 'X'
    elif p == 'o' or p == 'O':

        pg[i][j] = 'O'
    else:
        print('invalid input')
    Computer()
    printg()
    Winner()

def putC(p,i,j):
    if p == 'x' or p== 'X':
        pg[i][j] = 'X'
    elif p == 'o' or p == 'O':

        pg[i][j] = 'O'
    else:
        print('invalid input')
    Winner()

def Winner():
    for i in range(3):
        if pg[i][0] == pg[i][1] and pg[i][1] == pg[i][2] and (pg[i][0] == 'X' or pg[i][0] == 'O'):
            print(pg[i][0] + ' has won')
        elif pg[0][i] == pg[1][i] and pg[1][i] == pg[2][i] and (pg[i][0] == 'X' or pg[i][0] == 'O'):
            print(pg[0][i] + ' has won')
    if pg[0][0] == pg[1][1] and pg[1][1] == pg[2][2] and (pg[0][0] == 'X' or pg[1][1] == 'O'):
        print(pg[0][0] + ' has won')
    elif pg[0][2] == pg[1][1] and pg[1][1] ==  pg[2][0] and (pg[1][1] == 'X' or pg[1][1] == 'O'):
        print(pg[1][1] + ' has won')
        
def Computer():
    #######Defence System#######
    for i in range(3):
        #######Checking Each Row########
        if pg[i][0] == 'X' and pg[i][1] == 'X':
            putC('o',i,2)
        if pg[i][0] == 'X' and pg[i][2] == 'X':
            putC('o',i,1)
        if pg[i][1] == 'X' and pg[i][2] == 'X':
            putC('o',i,0)
        ##########Checking Each Column#####
        if pg[0][i] == 'X' and pg[1][i] == 'X':
            putC('o',2,i)
        if pg[0][i] == 'X' and pg[2][i] == 'X':
            putC('o',1,i)
        if pg[1][i] == 'X' and pg[2][i] == 'X':
            putC('o',0,i)
    ###########Checking Diagonal##########
    if pg[0][0] == 'X' and pg[1][1] == 'X':
        putC('o',2,2)
    if pg[0][0] == 'X' and pg[2][2] == 'X':
        putC('o',1,1)
    if pg[1][1] == 'X' and pg[2][2] == 'X':
        putC('o',0,0)
    #############Attacking System######
            
                
