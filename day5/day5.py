from functools import cmp_to_key
rule_dictionary = {}

def solve():
    sum = 0
    sum2 = 0
    grid = []
    with open("day5/input.txt", "r") as file:
        grid = list(map(list, file.read().split("\n")))
    start = (0,0)
    for y, r in enumerate(grid):
        for x, v in enumerate(r):
            if v == "^":
                start = (y,x,-1,0)
    pos = set()
    pos.add(start[0:2])
    print(pos)
    next_dy = {
        (-1,0):(0,1),
        (0,1):(1,0),
        (1,0):(0,-1),
        (0,-1):(-1,0)
    }
    y,x,dy,dx = start
    while len(grid) > start[0] >= 0  and len(grid[0]) > start[1] >= 0:
        if len(grid) > y + dy >= 0  and len(grid[0]) > x + dx >= 0:
            if(grid[y+dy][x+dx] == "#"):
                dy,dx = next_dy[(dy,dx)]
            y += dy
            x += dx
            pos.add(y,x)
        else:
            break
    sum = len(pos)


    return f"{sum}, {sum2}"
    
        