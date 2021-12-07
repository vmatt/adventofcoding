import re
file = open("input.txt", 'r').read()
file = file.split("\n")

##pt 1

horizontal = 0
depth = 0
for i,row in enumerate(file):
    c = row.split(" ")
    comm = c[0]
    mv = int(c[1])
    if comm == "forward":
        horizontal+=mv
    if comm == "up":
        depth-=mv
    if comm == "down":
        depth+=mv


print(horizontal*depth)
## pt2

horizontal = 0
depth = 0
aim = 0
for i,row in enumerate(file):
    c = row.split(" ")
    comm = c[0]
    mv = int(c[1])
    if comm == "forward":
        horizontal+=mv
        depth+=aim*mv
    if comm == "up":
        aim-=mv
    if comm == "down":
        aim+=mv


print(horizontal*depth)