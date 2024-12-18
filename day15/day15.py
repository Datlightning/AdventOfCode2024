from matplotlib.hatch import LargeCircles


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
    large_boxes = set()
    large_walls = set()
    x2 = 0
    pos2 = []
    for y,r in enumerate(grid):
        big_grid.append([])
        x2 = 0
        for x, v in enumerate(r):
            if v == "#":
                big_grid[y].append("#")
                big_grid[y].append("#")
                walls.add((y,x))
                large_walls.add((y,x2))
                large_walls.add((y,x2+1))
            elif v == "@":
                big_grid[y].append("@")
                big_grid[y].append(".")
                pos = [y,x]
                pos2 = [y,x2]
            elif v == "O":
                boxes.add((y,x))
                big_grid[y].append("[")
                big_grid[y].append("]")
                connected_boxes[(y,x2)] = (y,x2 + 1)
                connected_boxes[(y,x2 + 1)] = (y,x2)
                large_boxes.add((y,x2))
                large_boxes.add((y,x2 + 1))
            else:
                big_grid[y].append(".")
                big_grid[y].append(".")
            x2 += 2

    # display_grid(big_grid)
    # print(connected_boxes)
    for part2 in [False, True]:
        if part2:
            pos[0] = pos2[0]
            pos[1] = pos2[1]
        for i in instructions:
            if i == "\n":
                continue
            dy,dx = DIRS[i]
            # if part2:
            #     print(i)
            #     display(large_boxes, large_walls, pos, l*2, w)
            #     print()
            ny = dy + pos[0]
            nx = dx + pos[1]
            move = True
            if((ny,nx) in boxes if not part2 else large_boxes):
                if not part2:
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
                else:
                    q = [(ny,nx)]
                    push = []
                    seen = set()
                    while q:
                        cy,cx = q.pop()
                        if (cy,cx) in seen:
                            continue
                        seen.add((cy,cx))
                        if (cy,cx) in large_boxes:
                            ccy, ccx = connected_boxes[(cy,cx)]
                            push.append([(cy,cx), (ccy, ccx)])
                            q.append((cy + dy, cx + dx))
                            q.append((ccy + dy, ccx + dx))
                        elif (cy,cx) in large_walls:
                            move = False
                            break
                    else:
                        remove = set()
                        add = set()
                        new_box_pairs = []
                        for box1, box2 in push:
                            if box1 not in connected_boxes or box2 not in connected_boxes:
                                continue
                            del connected_boxes[box1]
                            del connected_boxes[box2]
                            remove.add(box1)
                            remove.add(box2)
                            box1y, box1x = box1
                            box2y, box2x = box2
                            add.add((box1y + dy, box1x + dx))
                            add.add((box2y + dy, box2x + dx))
                            new_box_pairs.append([(box1y + dy, box1x + dx),(box2y + dy, box2x + dx)])
                        large_boxes.difference_update(remove)
                        large_boxes = large_boxes | add
                        for box1, box2 in new_box_pairs:
                            connected_boxes[box1] = box2
                            connected_boxes[box2] =box1
            elif (ny,nx) in walls:
                continue
            if move:
                pos[0] += dy
                pos[1] += dx
        if not part2:
            for box in boxes:
                sum1 += box[0] * 100 + box[1]
        else:
            # display(large_boxes, large_walls, pos, l*2, w)
            seen =set()
            for box in large_boxes:
                if box in seen:
                    continue
                x = min(box[1], connected_boxes[box][1])
                seen.add(box)
                seen.add(connected_boxes[box])
                sum2 += box[0] * 100 + x 


    return f"{sum1}, {sum2}"

