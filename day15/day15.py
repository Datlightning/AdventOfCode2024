def display(boxes, walls, pos, l, w):
    for y in range(w):
        current = ""
        for x in range(l):
            if ((y,x) in boxes):
                current += "O"
            elif((y,x) in walls):
                current += "#"
            elif([y,x] == pos):
                current += "@"
            else:
                current += "."
        print(current)
def display_grid(g):
    for i in g:
        print("".join(i))
def solve():
    sum1 = 0  
    sum2 = 0
    grid = []
    instructions = []
    walls = set()
    boxes = set()
    pos = ()
    l = w = 0
    with open("day15/input.txt", "r") as file:
        grid, instructions =   file.read().split("\n\n")
        grid = [list(i) for i in grid.split("\n")]
        l = len(grid)
        w=  len(grid[0])
        # print(instructions)
        instructions = [i for i in instructions]
    DIRS = {
        ">":(0,1),
        "<":(0,-1),
        "v":(1,0),
        "^":(-1,0)
    }
    big_grid = []
    connected_boxes = {

    }
    x2 = 0
    for y,r in enumerate(grid):
        big_grid.append([])
        for x, v in enumerate(r):
            if v == "#":
                big_grid[y].append("#")
                big_grid[y].append("#")
                walls.add((y,x))
            elif v == "@":
                big_grid[y].append("@")
                big_grid[y].append(".")
                pos = [y,x]
            elif v == "O":
                boxes.add((y,x))
                big_grid[y].append("[")
                big_grid[y].append("]")
                connected_boxes[(y,x2)] = (y,x2 + 1)
                connected_boxes[(y,x2 + 1)] = (y,x2)
            else:
                big_grid[y].append(".")
                big_grid[y].append(".")
            x2 += 2
    display_grid(big_grid)
    print(connected_boxes)
    for i in instructions:
        if i == "\n":
            continue
        # display(boxes,walls, pos, l, w)
        dy,dx = DIRS[i]
        ny = dy + pos[0]
        nx = dx + pos[1]
        if((ny,nx) in boxes):
            push = []
            while (ny,nx) in boxes:
                push.append((ny,nx))
                ny += dy
                nx += dx
            if (ny,nx) in walls:
                continue
            else:
                remove = set()
                add = set()
                for boxy, boxx in push:
                    remove.add((boxy, boxx))
                    add.add((boxy + dy, boxx + dx))
                boxes.difference_update(remove)
                boxes = boxes | add
        elif (ny,nx) in walls:
            continue
        pos[0] += dy
        pos[1] += dx
   
    



    return f"{sum1}, {sum2}"

