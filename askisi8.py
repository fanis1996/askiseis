def Loadfile(inputfile):
    f = open(inputfile, 'r')
    s=""
    for line in f:
        s += line  
    s = s.splitlines()  
    f.close()
    return s
def RightRotation90(s,b):
    for i in range(8):
        for j in range(8):
            b[j][7-i]= s[i][j]
    for i in range(8):
        b[i] = ''.join(str(n)for n in b[i])
    return b
def LeftRotation90(s,b):
    for i in range(8):
        for j in range(8):
            b[7-j][i]= s[i][j]
    for i in range(8):
        b[i] = ''.join(str(n)for n in b[i])
    return b
def RotateBy180(s,b):
    for i in range(8):
        for j in range(8):
            b[7-i][7-j]= s[i][j]
    for i in range(8):
        b[i] = ''.join(str(n)for n in b[i])
    return b
def Output(outputfile,b):
    d = open(outputfile, "w")
    for i in range(8):
        b[i] += "\n"
        d.write(b[i])
    d.close()


outputlist =[[" " for x in range(8)] for x in range(8)]
c =raw_input("Select file : ")
input = Loadfile(c)
while True:
    a = raw_input("1.Rotation of 90 degree left\n2.Rotation of 90 degree right\n3.Rotation of 180 degree\n Select: ")
    if a == '1' :
        outputlist = LeftRotation90(input,outputlist) 
        break
    elif a =='2' :
        outputlist = RightRotation90(input,outputlist)
        break 
    elif a == '3' : 
        outputlist = RotateBy180(input,outputlist)
        break
    else :
        print "Invalid option.Please try again."
a = raw_input("Where u want to save it?(press space and enter if you want the same one as the input file)")
if a ==" " : Output(c,outputlist)
else : Output(a,outputlist)