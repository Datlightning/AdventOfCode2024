from collections import deque
import enum


def solve():
    sum = 0
    sum2 = 0
    width = 0
    height = 0
    next = {
        "X":"M",
        "M":"A",
        "A":"S"
    }
    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
        (1,1),
        (1,-1),
        (-1,1),
        (-1,-1)
    ]
    d = deque()
    d2 = deque()
    with open("day4/input.txt", "r") as file:
        lines = file.read().split("\n")
        height = len(lines)
        width = len(lines[0])
        for y, l in enumerate(lines):
            for x, pos in enumerate(l):
                # print(pos)
                if pos == "X":
                    for dy, dx in directions:
                        d.append((y,x,pos, dy, dx))
                if pos == "A":
                    d2.append((y,x,pos))
                   

    
    while d:
        ny,nx,value,dy,dx = d.pop()
        if(value == "S"):
            sum += 1
            continue
        if(ny + dy == height or ny + dy < 0):
            continue
        if(nx + dx == width or nx + dx < 0):
            continue
        if lines[ny + dy][nx + dx] == next[value]:
            d.append((ny + dy,nx + dx, next[value], dy,dx))
    while d2:
        ny,nx,value = d2.pop()
        if ny > 0 and ny < height - 1 and nx > 0 and nx < width - 1:
            if lines[ny - 1][nx - 1] == "M" and lines[ny+1][nx-1] == "M" and lines[ny - 1][nx + 1] == "S" and lines[ny + 1][nx + 1] =="S":
                sum2 += 1
            if lines[ny - 1][nx - 1] == "M" and lines[ny+1][nx-1] == "S" and lines[ny - 1][nx + 1] == "M" and lines[ny + 1][nx + 1] =="S":
                sum2 += 1    
            if lines[ny - 1][nx - 1] == "S" and lines[ny+1][nx-1] == "M" and lines[ny - 1][nx + 1] == "S" and lines[ny + 1][nx + 1] =="M":
                sum2 += 1
            if lines[ny - 1][nx - 1] == "S" and lines[ny+1][nx-1] == "S" and lines[ny - 1][nx + 1] == "M" and lines[ny + 1][nx + 1] =="M":
                sum2 += 1
        # print(f"({ny}, {nx}, {value})")
                

        
    
    

    return f"{sum}, {sum2}"
    
        