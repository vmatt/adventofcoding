from copy import deepcopy
file = open("04/input.txt", 'r').read()
file = file.split("\n\n")

##pt 1
rowlen = len(file[0])
flen = len(file)

games = file.pop(0).split(',')

def fill_arr_row(val):
    board = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]
    # for y in board:

board_list = []
for board in file:
    board = board.split("\n")
    board_arr = []
    for row in board:
        row = row.split(" ")
        row[:] = [x for x in row if x]
        board_arr.append(list(row))
    board_list.append(board_arr)

board_ids = list(range(0,len(board_list)))
def count_matches(last_num,board_id):
    global board_ids
    if board_id in board_ids:
        board = board_list[board_id]
        for y,row in enumerate(board):
            xc = 0
            for x,value in enumerate(row):
                if value == 'x':
                    xc += 1
            if xc == len(row):
                board_ids.remove(board_id)
                return calc_winning(board,last_num)
        for x in range(0,len(board)):
            yc = 0
            for y in range(0,len(board[0])):
                boardxy = board[y][x]
                if boardxy == 'x':
                    yc += 1
            if yc == len(board):
                board_ids.remove(board_id)
                return calc_winning(board,last_num)

def calc_winning(arr,last_num):
    sumall = 0
    for y,row in enumerate(arr):
        for x,value in enumerate(row):
            if value != 'x':
                sumall += int(value)
    sumall = int(sumall)
    last_num = int(last_num)
    ret = sumall*last_num
    return ret


board_copy = deepcopy(board_list)
last_num = ''
def play():
    for e,num in enumerate(games):
        for i,board in enumerate(board_list):
            for y,row in enumerate(board):
                for x,value in enumerate(row):
                    if value == num:
                        last_num = value
                        board_list[i][y][x] = 'x'
        winner = None
        winner = count_matches(num)
        if winner is not None:
            print(last_win)

def play2():
    last_win = ''
    for e,num in enumerate(games):
        last_num = num
        for i,board in enumerate(board_list):
            for y,row in enumerate(board):
                for x,value in enumerate(row):
                    if value == num:
                        last_num = value
                        board_list[i][y][x] = 'x'
            winner = None
            winner = count_matches(last_num,i)
            if winner is not None:
                last_win = winner
    print(last_win)


# w = play()
# print(w)
w = play2()
# calc_winning(w)



