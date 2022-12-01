from copy import deepcopy
file = open("input.txt",'r').read()
file=file.replace("\n","")
position = file.split(",")
position = [int(i) for i in position]
print(len(position))
del file
pos_len=len(position)

def takeSecond(elem):
    return elem[1]

distance=[]
for i in range(0,pos_len):
    r = []
    for j in range(0,pos_len):
        r.append(i)
    distance.append(r)
del r
distance2 = deepcopy(distance)

cost = []
cost2 = []
for i, dist in enumerate(distance):
    print(i) if i%100==0 else ""
    for j, vect in enumerate(dist):
        # pt2
        vector = abs(vect-position[j])
        expon = (vector*(vector+1))/2
        distance2[i][j]=expon
        distance[i][j]=vector
    sdi =sum(distance[i])
    sdi2 =sum(distance2[i])
    cost.append([i,sdi])
    cost2.append([i,sdi2])

cost.sort(key=takeSecond)
cost2.sort(key=takeSecond)
print("part 1:" +str(cost[0]))
print("part 2:" +str(cost2[0]))
