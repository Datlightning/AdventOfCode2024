from collections import deque
def calculate_cheats(grid,start, end, target_score, cheats, distances):
    output = set()
    R = len(grid)
    C = len(grid[0])
    DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
    y,x = start
    seen = set()
    q = deque([(0,y,x,None,None,None)])
    while q:
        score, y, x, cheat_start, cheat_end, cheat_time = q.popleft()
        assert cheat_end is None
        if score > target_score:
            continue
        if (y,x) == end:
            if cheat_end is None:
                cheat_end = (y,x)
            output.add((cheat_start, cheat_end))
        if((y,x,cheat_start, cheat_end, cheat_time) in seen):
            continue
        seen.add((y,x,cheat_start, cheat_end, cheat_time))

        if cheat_start is None:
            assert grid[y][x] != '#'
            q.append( (score, y,x, (y,x), None, cheats))
        if cheat_time is not None and grid[y][x] != "#":
            if (y,x) in distances and distances[(y,x)] + score <= target_score:
                output.add((cheat_start, (y,x)))
        if cheat_time == 0:
            continue
        for dy, dx in DIRS:
            ny, nx = dy + y, dx + x
            if 0<=ny<R and 0<=nx<C:
                if cheat_time is not None:
                    assert cheat_time > 0
                    q.append((score + 1, ny, nx, cheat_start, None, cheat_time - 1))
                elif grid[ny][nx] != "#":
                    q.append( (score + 1, ny, nx, cheat_start, cheat_end, cheat_time))
    return len(output)

def solve():
    sum1 = 0  
    sum2 = 0
    grid = []
    l = 0
    w = 0
    with open("day20/input.txt", "r") as file:
        grid =   file.read().split("\n")
        grid = [list(i) for i in grid]
        l = len(grid)
        w=  len(grid[0])
    end = ()
    start = ()
    q = []
    for y, r in enumerate(grid):
        for x, v in enumerate(r):
            if v == "S":
                start = (y,x)
            elif v == "E":
                end =  (y,x)
                q = deque([(0,y,x)])
    
    seen = {}
  
    
    
    while q:
        score,y,x = q.popleft()
        if  start == (y,x):
            max_score = score
            break
        if (y,x) in seen:
            continue
        seen[(y,x)] = score
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0<=ny<l and 0<=nx<w and grid[ny][nx] != "#":
                q.append((score + 1, ny, nx))
   
    save = 100
    target = max_score - save
    sum1 = calculate_cheats(grid, start, end, max_score - 100, 2, seen)
    print(sum1)
    sum2 = calculate_cheats(grid, start, end, max_score - 100, 20, seen)
    
    # print(seen)
    #1010258 is too low       
    return f"Sum 1: {sum1}\nSum 2: {sum2}"

