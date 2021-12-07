file = open("input.txt", 'r').read()
file = file.split("\n")

def slope(right,d2=False):
    tree = 0
    rowlen=len(file[0])
    currpos = 0
    for i,row in enumerate(file):
        # print(str(i)+row)
        row = list(row)
        if i>0:
            if d2 is True and i%2!=0:
                print(str(i)+("".join(row)))
                continue
            currpos+=right
            if currpos >= rowlen:
                currpos = currpos - rowlen
            if row[currpos]=="#":
                row[currpos]="X"
                tree+=1
            else:
                row[currpos] = "O"
        row = "".join(row)
        print(str(i)+row)
    return tree

a=slope(1)
b=slope(3)
c=slope(5)
d=slope(7)
e=slope(1,True)
print(a*b*c*d*e)



