file = open("input.txt", 'r').read()
elfs = file.split("\n\n")

# int_calories = [[int(y) if len(y)>0 else 0 for y in x.split('\n')] for x in elfs]
# sum_calories = {i+1:sum(x) for i,x in enumerate(int_calories)}
# sort_calories = dict(sorted(sum_calories.items(), key=lambda item: item[1], reverse=True))
#
# sort_calories = dict(sorted({i+1:sum(x) for i,x in enumerate([[int(y) if len(y)>0 else 0 for y in x.split('\n')] for x in elfs])}.items(), key=lambda item: item[1], reverse=True))
# print(f"Top elf calories: {list(sort_calories.values())[0]}")
# print(f"Top 3 elf calories: {sum(list(sort_calories.values())[:3])}")

sort_calories = dict(sorted({i+1:sum(x) for i,x in enumerate([[int(y) if len(y)>0 else 0 for y in x.split('\n')] for x in open("01/input.txt", 'r').read().split("\n\n")])}.items(), key=lambda item: item[1], reverse=True));

print(f"Top elf calories: {list(sort_calories.values())[0]}");print(f"Top 3 elf calories: {sum(list(sort_calories.values())[:3])}")

