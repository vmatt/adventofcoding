from copy import deepcopy
file = open("03/input.txt", 'r').read()
file = file.split("\n")

##pt 1
rowlen = len(file[0])
flen = len(file)

gamma = [0* i for i in range(rowlen)]
epsylon = [0* i for i in range(rowlen)]

# for i,row in enumerate(file):
#     for c,char in enumerate(row):
#         if row[c] == '1':
#             gamma[c]+=1
#         else:
#             epsylon[c]+=1
#
# gamma2 = ""
# for i, row in enumerate(gamma):
#     if float(gamma[i]) >= (flen/2):
#         gamma2 += "1"
#     else:
#         gamma2 += "0"
#
# epsylon2 = ""
# for i, row in enumerate(gamma):
#     if epsylon[i] >= flen/2:
#         epsylon2+= "1"
#     else:
#         epsylon2+= "0"
# gamma = "".join(gamma2)
# eps = "".join(epsylon2)
# gamma = int(gamma,2)
# eps = int(eps,2)
# print(gamma,eps,gamma*eps)


## pt2



gamma2 = ""
epsylon2 = ""

def o2f(arr,pos):
    o2 = []
    zeros = 0
    ones = 0
    mostcommon = ""
    for i, row in enumerate(arr):
        if row[pos] == '1':
            ones +=1
        else:
            zeros +=1
    if zeros > ones:
        mostcommon = '0'
    elif zeros <= ones:
        mostcommon = '1'
    for i, row in enumerate(arr):
        if row[pos] == mostcommon:
            o2.append(row)
    return o2

def co2f(arr,pos):
    co2 = []
    zeros = 0
    ones = 0
    leastcommon = ""
    for i, row in enumerate(arr):
        if row[pos] == '1':
            ones +=1
        else:
            zeros +=1
    if zeros > ones:
        leastcommon = '1'
    elif zeros <= ones:
        leastcommon = '0'
    for i, row in enumerate(arr):
        if row[pos] == leastcommon:
            co2.append(row)
    return co2

o2arr = []

for i in range (0,flen):
    if len(o2arr) == 1:
        break
    if i == 0:
        o2arr = (o2f(file, i))
    else:
        o2arr = o2f(o2arr, i)

co2arr = []
# flen = flen-1
for i in range (0,flen):
    if len(co2arr) == 1:
        break
    if i == 0:
        co2arr = (co2f(file, i))
    else:
        co2arr = co2f(co2arr, i)

oxi = int(o2arr[0],2)
co2 = int(co2arr[0],2)
print(oxi,co2,oxi*co2)
eps = "".join(epsylon2)
