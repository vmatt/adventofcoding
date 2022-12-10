file = open("input.txt", 'r')

def new_row():
    return ["." for _ in range (40)]

def update_sprite(start,finish,hashtag=True):
    char = '.'
    sprite = new_row()
    # handling overflow
    finish = finish if finish <40 else 39
    start = start if start >= 0 else 0
    if hashtag is True:
        char = '#'
    for c in range(start, finish):
        sprite[c] = char
    return sprite

def rl():
    global file
    row = file.readline().replace("\n","").split(" ")
    return int(row[1]) if len(row)==2 else None


screen = ""
rows = 0
register = 1
sprite = update_sprite(0,3)
crt_row = new_row()
cycle = 1
remaining_cycles = 1
last_action_finished = True
shift = None
running = True
print(f"Sprite_position: {''.join(sprite)}")
while running:
    if rows > 5:
        break
    cursor = cycle
    if last_action_finished:
        shift = rl()
        if shift:
            print(f"Start cycle   {cycle}: begin exectuting addx {shift}")
            remaining_cycles = 2
            last_action_finished = False
        else:
            remaining_cycles = 1

    print(f"During cycle  {cycle}: CRT draws pixel in position {cycle}")
    crt_row[cycle-1] = sprite[cycle-1]

    print(f"Current CRT row: {''.join(crt_row[0:cycle])}")
    if remaining_cycles<=1 and shift:
        register += shift
        sprite = update_sprite(register-1, register + 2)
        print(f"End of cycle  {cycle}: finish executing addx {shift}. Register is now {register}")
        print(f"Sprite_position: {''.join(sprite)}")
        last_action_finished = True
    print()
    remaining_cycles -= 1
    cycle+=1
    if cycle == 41:
        rows+=1
        screen += ''.join(crt_row[0:cycle])+"\n"
        cycle = 1
        crt_row = new_row()
        running = True

print(screen)
