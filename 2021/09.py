from copy import deepcopy
file = open("09/input.txt", 'r').read()
heatmap=file.split("\n")

def get_adj(pos, y, x):
    value = 9
    if pos == 'top':
        y = y-1
    elif pos == 'bottom':
        y = y+1
    elif pos == 'left':
        x = x - 1
    elif pos == 'right':
        x = x + 1
    if x >= 0 and y >= 0:
        try:
            value = int(heatmap[y][x])
        except:
            pass
    return value


def get_height(x,y):
    global heatmap
    try:
        return int(heatmap[y][x])
    except:
        return 9

basins=[]
low_values = ""
pt1 = 0
basin_id = 0
for y, row in enumerate(heatmap):
    for x, c in enumerate(row):
        c = int(c)
        if x == 0 and y ==36:
            print()
        top=get_adj('top', y, x)
        left=get_adj('left', y, x)
        right=get_adj('right', y, x)
        bottom=get_adj('bottom', y, x)

        if c < top and c < bottom and c < right and c < left:
            low_values+=f"{c}, x{x}y{y}\n"
            basins.append([x,y])
            c=c+1
            pt1+=c

# print(low_values)
print("pt1:", pt1)
print()

basin_dict = {x:0 for x in range(len(basins))}

visited_nodes = set()
def recursive_scan(x,y):
    size=0
    if f"{x},{y}" in visited_nodes or y < 0 or x < 0:
        return size
    else:
        visited_nodes.update([f"{x},{y}"])

    top = get_adj('top', y, x)
    left = get_adj('left', y, x)
    right = get_adj('right', y, x)
    bottom = get_adj('bottom', y, x)
    if top < 9:
        size+=recursive_scan(x,y-1)
    if bottom < 9:
        size+=recursive_scan(x,y+1)
    if left < 9:
        size+=recursive_scan(x-1,y)
    if right < 9:
        size+=recursive_scan(x+1,y)
    return size+1


kek = []
for i,b in enumerate(basins):
    original_x = b[0]
    original_y = b[1]
    start_point = get_height(x,y)
    c = deepcopy(start_point)
    x = deepcopy(original_x)
    y = deepcopy(original_y)
    size = recursive_scan(x,y)
    kek.append(size)

kek = sorted(kek,reverse=True)

na = 1
for i in kek[:3]:
    na = na*i

print(na)





