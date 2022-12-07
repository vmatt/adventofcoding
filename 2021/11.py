file = open("input.txt", 'r').read()
file = file.split("\n")
file.remove('')

import networkx as nx

matrix = []

def get_val(x,y):
    global matrix
    if y >= 0 and y <= y_len and x >= 0 and x <= x_len:
        return matrix[y][x]
    return -1

def inc_val(x,y):
    value = get_val(x,y)
    if 0 <= value < 9:
        matrix[y][x]+=1
    if value >= 9:
        matrix[y][x]=0
        inc_adj(x,y)

def inc_adj(yo, xo):
    global matrix,x_len,y_len
    top=0
    bottom=0
    left=0
    right=0
    leftbottom=0
    leftttop=0
    rightbottom=0
    righttop=0


    y = yo-1
    top = inc_val(xo,y)

    y = yo+1
    bottom = inc_val(xo,y)

    x = xo - 1
    left = inc_val(x,yo)

    x = xo + 1
    right = inc_val(x,yo)

    x = xo + 1
    y = yo+1
    rightbottom = inc_val(x,y)
    x = xo + 1
    y = yo - 1
    righttop = inc_val(x,y)

    x = xo - 1
    y = yo + 1
    leftbottom = inc_val(x,y)

    x = xo - 1
    y = yo - 1
    lefttop = inc_val(x,y)
    # return [top,bottom,left,right,righttop,rightbottom,lefttop,leftbottom]

for row in file:
    matrix.append([int(x) for x in row])

x_len = len(matrix[0])
y_len = len(matrix)

for x in range(x_len):
    for y in range(y_len):
        val = get_val(x,y)
        if val>=9:
            inc_adj(x,y)
        if val >= 0:
            inc_val(x,y)
print()

