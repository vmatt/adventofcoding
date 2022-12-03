file = open("03/input.txt", 'r').read()
file = file.split("\n")

def get_id(char):
    id = ord(char)
    if id > 96:
        id = id-96
    elif id <=96:
        id = id-64+26
    return id

sum_of_common = 0
for i,row in enumerate(file):
    row_len = int(len(row)/2)
    first_pack = row[0:row_len]
    second_pack = row[row_len:]
    first_pack = set(first_pack)
    second_pack = set(second_pack)
    common = first_pack.intersection(second_pack)

    for c in common:
       importance = get_id(c)
       sum_of_common+=importance
print(sum_of_common)


sum_of_common = 0
one=""
two=""
tre=""

file.remove('')
rows = len(file)

sum_of_common = 0
for i in range(0,rows,3):
    one = set(file[i])
    two = set(file[i+1])
    tre = set(file[i+2])
    common = one.intersection(two).intersection(tre)
    for c in common:
        importance = get_id(c)
        print(importance)
        sum_of_common+=importance
print("seoncd prt: ", sum_of_common)
