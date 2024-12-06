

from hmac import new


def expand(position):
    output = [position, (position[0] + position[2], position[1] + position[3], position[2], position[3])]
    return output
def solve():
    sum = 0
    sum2 = 0
    grid = []
    with open("day6/input.txt", "r") as file:
        grid = list(map(list, file.read().split("\n")))
    start = (0,0)
    grid_set = set()
    for y, r in enumerate(grid):
        for x, v in enumerate(r):
            if v == "^":
                start = (y,x,-1,0)
            grid_set.add((y,x))
    pos = set()
    pos.add(start[0:2])
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
            pos.add((y,x))
        else:
            break
    sum = len(pos)
    print(f"Part 1: {sum}")

    counter = 0
    position = set()
    for position in pos:
            counter += 1
            if(counter / 500 == counter // 500):
                print(counter)
            y,x,dy,dx = start
            new_positions = set()
            while True:
                if len(grid) > y + dy >= 0  and len(grid[0]) > x + dx >= 0:
                    if(grid[y+dy][x+dx] == "#" or (y+dy, x+dx) == (position[0:2])):
                        dy,dx = next_dy[(dy,dx)]
                    else: 
                        if((y,x,dy,dx) in new_positions):
                            sum2 += 1
                            break
                        new_positions.add((y,x,dy,dx))
                        y += dy
                        x += dx
                else:
                    break
    # sum2 = len(new_pos)


    return f"{sum}, {sum2}"
    
        