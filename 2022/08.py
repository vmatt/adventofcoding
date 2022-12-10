from copy import deepcopy

file = open("input.txt", 'r').read()
treemap = file.split("\n")
treemap.remove("")

def get_height(x,y):
    global treemap
    try:
        return int(treemap[y][x])
    except:
        return -1

def get_direction(a,b,step,target_value, xory):
    if xory=="y":
        for y2 in range(a,b,step):
            p = get_height(x,y2)
            if p >= target_value:
                return False
    if xory == "x":
        for x2 in range(a, b, step):
            p = get_height(x2, y)
            if p >= target_value:
                return False
    return True

def get_visible_distance(a,b,step,target_value, xory,x,y):
    cnt = 0
    if xory=="y":
        for y2 in range(a,b,step):
            p = get_height(x,y2)
            p = p if p > -1 else 999
            if p == 999:
                break
            elif p < target_value:
                cnt+=1
            elif p >= target_value:
                cnt+=1
                break
    if xory == "x":
        for x2 in range(a, b, step):
            p = get_height(x2, y)
            p = p if p > -1 else 999
            if p == 999:
                break
            elif p < target_value:
                cnt+=1
            elif p >= target_value:
                cnt += 1
                break
    return cnt

def get_visibility(x,y):
    global x_len,y_len
    target_value = get_height(x,y)
    # top
    is_visible = get_direction(y - 1, -1,-1,target_value, 'y')
    if is_visible:
        return True
    # bottom
    is_visible = get_direction(y+1, y_len,1, target_value, 'y')
    if is_visible:
        return True
    # left
    is_visible = get_direction(x-1, -1,-1, target_value, 'x')
    if is_visible:
        return True
    # right
    is_visible = get_direction(x + 1, x_len,1, target_value,'x')
    if is_visible:
        return True
    return False

def get_scenic(x, y):
    target_value = get_height(x, y)
    global x_len, y_len
    top = get_visible_distance(y - 1, -1, -1, target_value, 'y', x,y)
    bottom = get_visible_distance(y + 1, y_len, 1, target_value, 'y', x,y)
    left = get_visible_distance(x - 1, -1, -1, target_value, 'x', x,y)
    right = get_visible_distance(x + 1, x_len, 1, target_value, 'x', x,y)

    score = top*bottom*left*right
    return score

visible_nodes = set()
x_len = len(treemap[0])
y_len = len(treemap)

y = 3
x = 3

counter = 0

for y, row in enumerate(treemap):
    for x, c in enumerate(row):
        is_visible = get_visibility(x,y)
        if is_visible:
            counter +=1
print("pt1", counter)

# pt 2

best_tree = set()
d = get_scenic(2,1)
for y, row in enumerate(treemap):
    for x, c in enumerate(row):
        distance = get_scenic(x,y)
        best_tree.update([distance])



print("pt2", max(best_tree))

