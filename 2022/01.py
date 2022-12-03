sort_calories = dict(sorted({i+1:sum(x) for i,x in enumerate([[int(y) if len(y)>0 else 0 for y in x.split('\n')] for x in open(
    "01/input.txt", 'r').read().split("\n\n")])}.items(), key=lambda item: item[1], reverse=True)); print(f"Top elf calories: {list(sort_calories.values())[0]}");print(f"Top 3 elf calories: {sum(list(sort_calories.values())[:3])}")

