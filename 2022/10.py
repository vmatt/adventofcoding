from copy import deepcopy

file = open("input.txt", 'r')

def new_row():
    return ["." for _ in range (40)]
current_px = 1
last_step = ""
cycles = [1]
register=[1]
screen = []
row = file.readline()
print(f"Start cycle {cycles[-1]}")
print(f"During cycle {cycles[-1]}: draws pixel in position {current_px}")
register_px="#"
current_row = 0
screen.append(new_row())
while row:
    print(f"Start cycle {cycles[-1]}")
    row = row.split()
    if len(row)==2:
        add_nr = int(row[1])
        for c in (1,2):
            cycles.append(cycles[-1]+c)
            register.append(current_px)
        current_px += add_nr
    else:
        cycles.append(cycles[-1]+1)
        register.append(current_px)
    row = file.readline()
if current_px != register[-1]:
    cycles.append(cycles[-1]+1)
    register.extend([current_px])
total = 0
for r in [20,60,100,140,180,220]:
    total += r*register[r]
print(total)
