import re
file = open("01/input.txt", 'r').read()
file = file.split("\n")

# seats = [x[:] for x in [["O"] * 8] * 128]
inc = 0
for i,row in enumerate(file):
    rn = int(file[i])
    try:
        rb = int(file[i - 1])
    except:
        rb = 0
    if rn > rb:
        inc+=1
print(inc)


file = open("01/input.txt", 'r').read()
f = file.split("\n")
f = [int(s) for s in f]

# seats = [x[:] for x in [["O"] * 8] * 128]
inc = 0
for i in range (2,len(f)):
    now = [f[i]+f[i-1]+f[i-2]]
    try:
        before = [f[i-1]+f[i-2]+f[i-3]]
    except:
        before = [f[i]+f[i-1]+f[i-2]]
    if now > before:
        inc+=1
print(inc)
