file = open("input.txt",'r').read()
file = file.split("\n")

validpass = 0
for row in file:
    row = row.split(": ")
    policy = row[0].split(" ")
    char = policy[1]
    occ = policy[0].split("-")
    min = int(occ[0])
    max = int(occ[1])
    pw = row[1]
    ccount = 0
    for c in pw:
        if c == char:
            ccount+=1
    if ccount <= max and ccount >= min:
        validpass+=1

print("part1: "+str(validpass))


validpass = 0
for row in file:
    row = row.split(": ")
    policy = row[0].split(" ")
    char = policy[1]
    occ = policy[0].split("-")
    min = int(occ[0])
    max = int(occ[1])
    pw = row[1]
    ccount = 0
    for i,c in enumerate(pw):
        a=i+1
        if (a == min or a == max) and c == char:
            ccount+=1
    if ccount == 1 :
        validpass+=1

print("part2: "+str(validpass))
