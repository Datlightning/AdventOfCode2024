
def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    l = 0
    w = 0
    
    with open("day10/input.txt", "r") as file:
        g =  [list(map(int, list(i))) for i in file.read().split("\n")]
        w = len(g)
        l = len(g[0])
    queue = []
    for y, row in enumerate(g):
        for x, v in enumerate(row):
            if v == 0:
                queue.append((y,x,0))
    successful_target = set()
    while queue:
        cy,cx,value = queue.pop()
        if(value == 0):
            sum1 += len(successful_target)
            successful_target = set()
        if(value == 9):
            sum2 += 1
            successful_target.add((cy,cx))
            continue
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= cy + dy < w and 0<=cx + dx < l and g[dy + cy][dx + cx] == value + 1:
                queue.append((cy + dy, cx + dx, value + 1))
    sum1 += len(successful_target)   

   

    return f"{sum1}, {sum2}"
