from heapq import heappop, heappush
def display(path, l, w):
    for y in range(w):
        string =""
        for x in range(l):
            if (y,x) in path:
                string += "#"
            else:
                string += "."
        print(string)

def solve():
    sum1 = 0  
    sum2 = 0
    grid = []
    q = []
    
    with open("day16/input.txt", "r") as file:
        grid =   file.read().split("\n")
        grid = [list(i) for i in grid]
        l = len(grid)
        w=  len(grid[0])
    for y, r in enumerate(grid):
        for x, v in enumerate(r):
            if v == "S":
                heappush(q, ( 0, y,x, 0, 1,[(y,x)]))

    
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = dict()
    path = set()
    sum2 = 0
    while q:
        score, y, x, dy, dx, currentpath = heappop(q)
        # display(currentpath, l, w)
        # print(count)
        
        if grid[y][x] == "E":
            # print((y,x))
            # print(score)          
            if sum1 == 0:
                sum1 = score
            if score == sum1:
                # display(set(currentpath), l, w)
                path = path | set(currentpath)
                # print(len(path))
            continue
        if score > sum1 > 0:
            continue
        if((y,x,dy,dx) in seen and seen[(y,x,dy,dx)] < score):
            continue
        seen[(y,x,dy,dx)] = score
        ny = y + dy
        nx = x + dx
        if 0<=nx<l and 0<=ny<w and grid[ny][nx] != "#":
            heappush(q, (score + 1, ny, nx, dy, dx, currentpath + [(ny,nx)]))
        for ndy, ndx in DIRS:
            if (dy,dx) != (-ndy, -ndx) and (dy,dx) != (ndy,ndx):
                heappush(q, (score + 1000, y, x, ndy, ndx, currentpath))
       
    sum2 = len(path)
    display(path,l,w)



    return f"{sum1}, {sum2}"

