file = open("04/input.txt", 'r').read()
file = file.split("\n")

for i,row in enumerate(file):
    row_len = int(len(row)/2)
