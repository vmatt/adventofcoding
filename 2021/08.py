mapp = ["abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg"]
from copy import deepcopy
file = open("08/input.txt", 'r').read()
file=file.split("\n")
file.pop(-1)

# for row in file:
#     row = row.split(" | ")
#     inp = row[0].split(" ")
#     out = row[1].split(" ")
#     con = inp+out
#     if (len(max(con,key=len))) < 7:
#         print(con)

count = 0
for row in file:
    row = row.split(" | ")
    inp = row[0].split(" ")
    out = row[1].split(" ")
    con = inp+out
    m4pp = deepcopy(mapp)
    letter = {"a":"",
              "b":"",
              "c":"",
              "d":"",
              "e":"",
              "f":"",
              "g":""}
    con = sorted(con,key=len)
    for p in con:
        # p = "".join(sorted(p))
        #if 1
        if len(p) == 2:
            for i,c in enumerate(p):
                if letter[mapp[1][i]] == '':
                    letter[mapp[1][i]]=c
            m4pp[1] = p
            count+=1
        # if 7
        elif len(p) == 3:
            for i,c in enumerate(p):
                if letter[mapp[7][i]] == '':
                    letter[mapp[7][i]]=c
            m4pp[7] = p
            count+=1
        # if 4
        elif len(p) == 4:
            for i,c in enumerate(p):
                if letter[mapp[4][i]] == '':
                    letter[mapp[4][i]]=c
            m4pp[4] = p
            count+=1
        # if 8
        elif len(p) == 7:
            for i,c in enumerate(p):
                if letter[mapp[8][i]] == '':
                    letter[mapp[8][i]]=c
            m4pp[8] = p
            count+=1

print("kek")





