import dis


def display(grid):
    for i in grid:
        print("".join(i))
def display(grid, set):

    for y,r in enumerate(grid):
        current = ""
        for x, v in enumerate(r):
            if((y,x) in set):
                current += "."
            else:
                current +=v 
        print(current)

def expand(point, l, w, g,v, p1):
    y,x = point
    output = []
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=y+dy<w and 0<=x+dx<l and g[y+dy][x+dx] == v:
            output.append((y+dy, x+dx))
        else:
            p1 += 1
    
    return output, p1
def calculate_edges(g,w,l):
    output = 0
    for y in range(w):
        
        for x in range(l):
            left_pos = (y,x+1)
            down_pos = (y+1,x)
            

    return output
def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    l = 0
    w = 0
    seen = set()
    p1 = 0
    a1 = 0
    with open("day12/input.txt", "r") as file:
        g =  [list(i) for i in file.read().split("\n")]
        w = len(g)
        l = len(g[0])
    # display(g)
    for y, r in enumerate(g):
        for x, v in enumerate(r):
            a1 = 0
            p1 = 0
            p2 = 0
            if (y,x) in seen:
                continue
            q = [(y,x)]
            current = set()
            while q:
                cy,cx = q.pop()
                if (cy,cx) in seen:
                    continue
                seen.add((cy,cx))
                a1 += 1
                current.add((cy,cx))
                expanded, p1 = (expand((cy,cx), l, w,g,v, p1))
                q.extend(expanded)

            display(g, current)
            p2 = calculate_edges(current,w,l)
            print(v)
            print(a1)
            print(p1)
            print(p2)
            sum1 += a1 * p1
            sum2 += a1 * p2
            # print("")
    # print(a1 * p1)


    return f"{sum1}, {sum2}"

