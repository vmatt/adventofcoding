# from copy import deepcopy
# file = open("input.txt", 'r').read()
# file = file.split("\n")
#
# ##pt 1
# xmax = 0
# ymax = 0
#
# vents = []
# for row in file:
#     row = row.split(" -> ")
#     x1 = int(row[0].split(',')[0])
#     y1 = int(row[0].split(',')[1])
#     x2 = int(row[1].split(',')[0])
#     y2 = int(row[1].split(',')[1])
#     vents.append([x1,y1,x2,y2])
#     if x1>xmax:
#         xmax=x1
#     if x2>xmax:
#         xmax=x2
#     if y1>ymax:
#         xmax=y1
#     if y2>ymax:
#         ymax=y2
#
# fieldwidth = [0 * i for i in range(xmax+1)]
# fields = [deepcopy(fieldwidth) for i in range(ymax+1)]
# del fieldwidth,xmax,ymax,row,file
# maxpoint = 0
# for c in vents:
#     x1 = c[0]
#     y1 = c[1]
#     x2 = c[2]
#     y2 = c[3]
#     if y1 == y2:
#         if x1>x2:
#             for x in range (x2,x1+1):
#                 fields[y1][x] += 1
#                 val = (fields[y1][x])
#                 if val > maxpoint:
#                     maxpoint = val
#         else:
#             for x in range(x1,x2+1):
#                 fields[y1][x] += 1
#                 val = (fields[y1][x])
#                 if val > maxpoint:
#                     maxpoint = val
#     if x1 == x2:
#         if y1 > y2:
#             for y in range(y2,y1+1):
#                 fields[y][x1] += 1
#                 val = (fields[y][x1])
#                 if val > maxpoint:
#                     maxpoint = val
#         else:
#             for y in range(y1, y2+1):
#                 fields[y][x1]  += 1
#                 val = (fields[y][x1])
#                 if val > maxpoint:
#                     maxpoint = val
#
#
# vent_count=0
# for y,row in enumerate(fields):
#     for x, val in enumerate(row):
#         if val > 1:
#             vent_count+=1
#
#
# print(maxpoint,vent_count)
#
#


from copy import deepcopy

file = open("input.txt", 'r').read()
file = file.split("\n")

##pt 1
xmax = 0
ymax = 0

vents = []
for row in file:
    row = row.split(" -> ")
    x1 = int(row[0].split(',')[0])
    y1 = int(row[0].split(',')[1])
    x2 = int(row[1].split(',')[0])
    y2 = int(row[1].split(',')[1])
    vents.append([x1, y1, x2, y2])
    if x1 > xmax:
        xmax = x1
    if x2 > xmax:
        xmax = x2
    if y1 > ymax:
        xmax = y1
    if y2 > ymax:
        ymax = y2

# for v1 in vents:
#     for v2 in vents:
#         if v1[0] == v2[2] and v1[3] == v2[3] and v1[2] == v2[0] and v1 != v2:
#             vents.remove(v2)
#             print(v1)

fieldwidth = [0 * i for i in range(xmax + 1)]
fields = [deepcopy(fieldwidth) for i in range(ymax + 1)]
del fieldwidth, xmax, ymax, row, file
maxpoint = 0
for c in vents:
    x1 = c[0]
    y1 = c[1]
    x2 = c[2]
    y2 = c[3]
    if y1 == y2:
        if x1 > x2:
            for x in range(x2, x1 + 1):
                fields[y1][x] += 1
        else:
            for x in range(x1, x2 + 1):
                fields[y1][x] += 1
    if x1 == x2:
        if y1 > y2:
            for y in range(y2, y1 + 1):
                fields[y][x1] += 1
        else:
            for y in range(y1, y2 + 1):
                fields[y][x1] += 1

    if y1 < y2:
        if x1 > x2:
            for i,x in enumerate(range(x1, x2-1,-1)):
                fields[y1+i][x] += 1
        if x1 < x2:
            for i,x in enumerate(range(x1, x2 + 1)):
                fields[y1+i][x] += 1
    if y1 > y2:
        if x1 > x2:
            for i,x in enumerate(range(x1, x2-1,-1)):
                fields[y1-i][x] += 1
        if x1 < x2:
            for i,x in enumerate(range(x1, x2 + 1)):
                fields[y1-i][x] += 1


vent_count = 0
for y, row in enumerate(fields):
    for x, val in enumerate(row):
        if val > 1:
            vent_count += 1
print("Part 2")
print(maxpoint, vent_count)


