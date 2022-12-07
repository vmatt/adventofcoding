file = open("input.txt", 'r').read()
datastreams = file.split("\n")
datastreams.remove("")

for d in datastreams:
    for i in range(0,len(d)-4,1):
        part = d[i:i+4]
        part_set = set(part)
        if len(part)==len(part_set) and len(part)==4:
            print(i+4)
            print(part,part_set)
            break


for d in datastreams:
    for i in range(0,len(d)-14,1):
        part = d[i:i+14]
        part_set = set(part)
        if len(part)==len(part_set) and len(part)==14:
            print(i+14)
            print(part,part_set)
            break
