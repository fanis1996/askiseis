from random import randint
stage = [[" " for x in range(10)] for x in range(20)]
c=0
Play = True
def addL(y):
    for i in range(3):
        stage[i][y]="0"
        if i ==2 :
            stage[i][y+1]="0"
def removeRow(Row):
    for i in range(Row+1,0):
        if i != 0 : stage[i] = stage[i-1] 
        else : stage[i]={" "," "," "," "," "," "," "," "," "," "}
def MoveDown(x,y):
    stage[x][y]=" "
    stage[x+2][y+1]=" "
    for i in range(2):
        stage[x+3][y+i]="0"
def Col(x,y):
    if stage[x][y] == "0" or stage[x][y+1] == "0":
        return True
    else:
        return False
while Play == True:
    RN = randint(0,8)
    for i in range(20):
        if i<2:
            if Col(i,RN)==True:
                Play = False
                break
            else:
                continue
        elif i==2:
            if Col(i, RN) == True:
                Play = False
                break
            else:
                c+=1
                addL(RN)
                continue
        else:
            if Col(i, RN) == True:
                break
            else:
                MoveDown(i-3, RN)
        if stage[i] == {"0","0","0","0","0","0","0","0","0","0"}:
            removeRow(i)
print c