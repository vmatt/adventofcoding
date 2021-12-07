import os

file = open("input.txt",'r').read()
file = file.split("\n")

for i in file:
    i = int(i)
    for n in file:
        n = int(n)
        for j in file:
            j = int(j)
            if i+n+j == 2020:
                print(i*n*j)
