file = open("02/input.txt", 'r').read()
file = file.split("\n")

##pt 1
op_move ={'A': 'Rock',
          'B': 'Paper',
          'C': 'Scissors'}
me_move ={'X': 'Rock',
          'Y': 'Paper',
          'Z': 'Scissors'}

matrix = [
    ['Rock', 'Scissors', 'op'],
    ['Rock', 'Paper', 'me'],
    ['Paper', 'Rock', 'op'],
    ['Paper', 'Scissors', 'me'],
    ['Scissors', 'Rock', 'me'],
    ['Scissors', 'Paper', 'op']
]

def eval_match(op,me):
    winner = ''
    if op == me:
        winner='draw'
    for r in matrix:
        if r[0] == op and r[1] == me:
            winner = r[2]
    return winner

def add_points(games,winner,opmove,mymove):
    if winner == 'draw':
        games['me']+=3
        games['op']+=3
    else:
        games[winner]+=outcome[winner]
    games['me'] += symbol_point[mymove]
    games['op'] += symbol_point[opmove]
    return games

symbol_point = {'Rock':1,
                'Paper':2,
                'Scissors':3}
outcome = {'me':6,
           'op':0,
           'draw':3}

games = {'me':0,'op':0}
for i,row in enumerate(file):
    if len(row)==0:
        continue
    op,me = row.split(" ")
    opmove,mymove = op_move[op],me_move[me]
    winner = eval_match(opmove,mymove)
    games = add_points(games,winner,opmove,mymove)
print(games)

## PT2

me_move_2 ={'X': 'Lose',
          'Y': 'Draw',
          'Z': 'Win'}

win = {'Rock': 'Paper',
        'Paper': 'Scissors',
        'Scissors':'Rock'}
lose = {'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'}

def eval_recommended(op,me):
    if me == 'X':
        mymove = lose[op_move[op]]
    elif me == 'Y':
        mymove = op_move[op]
    elif me=='Z':
        mymove = win[op_move[op]]
    return mymove

games = {'me':0,'op':0}
for i,row in enumerate(file):
    if len(row)==0:
        continue
    op,me = row.split(" ")
    mymove = eval_recommended(op,me)
    opmove = op_move[op]
    winner = eval_match(opmove,mymove)
    games = add_points(games, winner, opmove, mymove)
print(games)
