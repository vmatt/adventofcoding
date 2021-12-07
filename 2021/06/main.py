file = open("input.txt",'r').read()
file = file.split("\n")

# +1 for buffer
fishes = [0 for i in range(0,10)]
# load starting fish values
for row in file:
    for i,timer in enumerate(row.split(",")):
        if timer != '':
            timer = int(timer)
            fishes[timer]+=1

iteration = 256
# for calculate proper iter value, adding +2 is needed for the iteration
for day in range(1,iteration+2):
    for i in range(1, len(fishes)):
        if fishes[0]>0 and i == 1:
            fishes[7]+=fishes[0]
            fishes[9]+=fishes[0]
            fishes[0]=0

        if fishes[i]>0:
            fishes[i-1]+=fishes[i]
            fishes[i]=0

s = 0
for i in range(0,8):
    s+=fishes[i]

print(s)