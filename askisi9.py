from random import randint
stage = [[" " for x in range(20)] for x in range(10)]
c=0
Play = True
def addL(x,y):
    for i in range(3):
        stage[x+i][y]="0"
        if i ==2 :
            stage[x+2][y+1]="0"
while Play == True:
    RN = randint(0,18)
    for i in range(10):
        if stage[i][RN] == "0" or stage[i][RN+1] == "0":
            if i-3 < 0 :
                Play =False
                break
            else :
                addL(i-3, RN)
                c+=1
                break
        elif i == 9 :
            addL(i-3, RN)
            c+=1
            break
print c