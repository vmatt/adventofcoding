import math

with open('10/input.txt', 'r') as r:
    file = r.read()
    file = file.split("\n")
    file.remove("")

close_points = {
    ')': 3,
    ']':57,
    '}':1197,
    '>':25137
}

close_err_cnt = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}
open_pairs = {
    '(': ')',
    '[':']',
    '{':'}',
    '<':'>'
}

open_symbols = open_pairs.values()


for i,row in enumerate(file):
    used = []
    pos=0
    check = True
    while check:
        if pos >= len(row):
            break
        c = row[pos]
        used.append(c)
        pos+=1
        if len(used)>1:
            if c not in open_symbols:
                for j in range(len(used)-2,0,-1):
                    preceeding = used[j]
                    try:
                        expected_closer = open_pairs[preceeding]
                        break
                    except:
                        pass

                if expected_closer==c:
                    used.pop(j)
                    used.pop(-1)
                else:
                    check=False
                    print(row)
                    print(pos)
                    print(f"expected {expected_closer} got {c}")
                    close_err_cnt[c]+=1

pt1 = []
for symbol,cnt in close_err_cnt.items():
    calc = cnt*close_points[symbol]
    pt1.append(calc)
    print(symbol,calc)

print(sum(pt1))


## Part 2
all_solved = []
for i,row in enumerate(file):
    used = []
    pos=0
    closing=""
    check = True
    while check:
        if pos >= len(row):
            break
        c = row[pos]
        used.append(c)
        pos += 1
        if pos == len(row)-1:
            print("")
        if len(used) > 1:
            if c not in open_symbols:
                for j in range(len(used) - 2, 0, -1):
                    preceeding = used[j]
                    try:
                        expected_closer = open_pairs[preceeding]
                        break
                    except:
                        pass
                if expected_closer == c:
                    used.pop(j)
                    used.pop(-1)
                else:
                    print(f"expected {expected_closer} got {c}")
                    closing+=expected_closer
    used.reverse()
    solved_closers = []
    fail=False
    for u in used:
        try:
            solved_closers.append(open_pairs[u])
        except:
            # If it contains unresolvable pattern then ignore the row
            fail=True
    if not fail:
        print("".join(solved_closers))
        all_solved.append(solved_closers)


close_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

total_total = []
for row in all_solved:
    total_score = 0
    for c in row:
        total_score = total_score*5+close_points[c]
    total_total.append(total_score)

total_total_total = sorted(total_total)

id = math.floor(len(total_total_total)/2)
print(total_total_total[id])
