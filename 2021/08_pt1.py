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
    letter = {"a":"a",
              "b":"b",
              "c":"c",
              "d":"d",
              "e":"e",
              "f":"f",
              "g":"g"}
    for p in con:
        p = "".join(sorted(p))
        #if 1
        if len(p) == 2:
            for i,c in enumerate(p):
                letter[mapp[1][i]]=c
            m4pp[1] = p
            count+=1
        # if 7
        elif len(p) == 3:
            for i,c in enumerate(p):
                letter[mapp[7][i]]=c
            m4pp[7] = p
            count+=1
        # if 4
        elif len(p) == 4:
            for i,c in enumerate(p):
                letter[mapp[4][i]]=c
            m4pp[4] = p
            count+=1
        # if 8
        elif len(p) == 7:
            for i,c in enumerate(p):
                letter[mapp[8][i]]=c
            m4pp[8] = p
            count+=1
    inv_letter = {v: k for k, v in letter.items()}
    # if len(inv_letter) != len(letter):
    #     mk = set(letter.keys())-set(letter.values())
    #
    #     mk = list(mk)
    #     mv = list(mv)
    #     for i,k in enumerate(mk):
    #         letter[k] = mv[i]
    # else:
    #     print("eh")

    for i,m in enumerate(mapp):
        if i not in (1,4,7,8):
            m = list(m4pp[i])
            for j,c in enumerate(m):
                m[j]=letter[c]
            m4pp[i] = "".join(m)
    num = ""
    for o in out:
        o = set(o)
        for i,m in enumerate(m4pp):
            m = set(m)
            dif = o-m
            if len(dif) == 0 and len(o) == len(m):
                num+=str(i)
    print(int(num))





