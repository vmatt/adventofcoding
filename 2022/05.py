file = open("input.txt", 'r').read()

stacks, instructions = file.split("\n\n")
stacks = stacks.split("\n")
stack_ids = stacks[-1].replace(" ", "").split("  ")[0]
stack_tracker = {int(id): [] for id in stack_ids}
stacks.pop(-1)

for row in stacks:
    splitted_by_cols=[]
    for id in range(0,len(row),4):
        c = row[id:id+4]
        splitted_by_cols.append(c[1])
    for id, col in enumerate(splitted_by_cols):
        if col != "" and col !=' ':
            stack_tracker[id+1].append(col)

for v in stack_tracker.values():
    v.reverse()

instructions = instructions.replace("move ","").replace("from ","").replace("to ","")
instructions = instructions.split("\n")
instructions.remove("")
for inst in instructions:
    move, crate_from, crate_to = inst.split(" ")
    move, crate_from, crate_to = int(move), int(crate_from), int(crate_to)
    lifted_crates = stack_tracker[crate_from][-move:]
    del stack_tracker[crate_from][-move:]
    # part 2
    stack_tracker[crate_to].extend(lifted_crates)
    # part 1
    # lifted_crates.reverse()
    # for crate in lifted_crates:
    #     stack_tracker[crate_to].append(crate)


for k, v in stack_tracker.items():
    print(v[-1], end="")

print()
print("fin")

