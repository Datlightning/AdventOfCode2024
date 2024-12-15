
from scipy.fftpack import cs_diff
from sympy import per


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

def expand(point, l, w, g,v, p1, perimeter):
    y,x = point
    output = []
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=y+dy<w and 0<=x+dx<l and g[y+dy][x+dx] == v:
            output.append((y+dy, x+dx))
        else:
            #this breaks it for a reason beyond me
            if (dy,dx) not in perimeter:
                perimeter[(dy,dx)] = set()
            perimeter[(dy,dx)].add((y, x))
            p1 += 1
    # print(p1)
    # print(output)
    
    return output, p1, perimeter

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
            # print(v)
            a1 = 0
            p1 = 0
            p2 = 0
            if (y,x) in seen:
                continue
            q = [(y,x)]
            perimeter = dict()
            current = set()
            while q:
                cy,cx = q.pop()
                if (cy,cx) in seen:
                    continue
                seen.add((cy,cx))
                a1 += 1
                current.add((cy,cx))
                expanded, p1, perimeter = (expand((cy,cx), l, w,g,v, p1, perimeter))
                q.extend(expanded)

            #     print("")
            # display(g, current)
            # print(v)
            # print(f"A1: {a1}")

            # print(f"P1: {p1}")
            p2 = 0
            for k, points in perimeter.items():
                # print(k)
                # print(points)
                seen_perimeter = set()
                for y2,x2 in points:
                    if (y2,x2) not in seen_perimeter:
                        # seen_perimeter.add((y,x))
                        p2 += 1
                        q = [(y2,x2)]
                        while q:
                            cy,cx = q.pop()
                            if (cy,cx) in seen_perimeter:
                                continue
                            seen_perimeter.add((cy,cx))
                            for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                                ny = dy + cy
                                nx = dx + cx
                                if ((ny,nx) in points):
                                    q.append((ny,nx))

            
            # print(f"A1: {a1}")

            # print(f"P1: {p1}")

            # print(f"P2: {p2}")
            sum1 += a1 * p1
            sum2 += a1 * p2
            # print("")
    # print(a1 * p1)


    return f"{sum1}, {sum2}"

