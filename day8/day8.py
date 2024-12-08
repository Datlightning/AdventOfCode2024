
from turtle import pos


def distance(node1, node2):
    return((node1[0] - node2[0], node1[1] - node2[1]), (node2[0] - node1[0], node2[1] - node1[1]))
def calculate_antinodes(v, l, w, p2):
    output = set()
    for i, v1 in enumerate(v):
        for _, v2 in enumerate(v[i+1:]):
            vec1 ,vec2  =  distance(v2,v1)
            dy1, dx1 = vec1
            dy2, dx2 = vec2
            if(p2):
                output.add(v2)
                cy, cx = v2
                while True:
                    if 0<=cy+dy1<w and 0<=cx+dx1<l:
                        output.add((cy + dy1, cx+ dx1))
                        cy += dy1
                        cx += dx1
                    else:
                        break
                # print(output)
                pass
            else:
                if 0<=v2[0]+dy1<w and 0<=v2[1]+dx1<l:
                    output.add((v2[0] + dy1, v2[1] + dx1))
            if(p2):
                output.add(v1)
                cy, cx =v1
                while True:
                    if 0<=cy+dy2<w and 0<=cx+dx2<l:
                        output.add((cy + dy2, cx + dx2))    
                        cy += dy2
                        cx += dx2
                    else:
                        break
                # print(output)
                pass
            else:
                if 0<=v1[0]+dy2<w and 0<=v1[1]+dx2<l:
                    output.add((v1[0] + dy2, v1[1] + dx2))    
    return output

def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    l = 0
    w = 0
    with open("day8/input.txt", "r") as file:
        g = [list(i) for i in file.read().split("\n")]
        w = len(g)
        l = len(g[0])
    nodes = {}
    for y, r in enumerate(g):
        for x, v in enumerate(r):
            if v == ".":
                continue
            if v in nodes:
                nodes[v].append((y,x))
            else:
                nodes[v] = [(y,x)]
    positions = set()
    posistion2 = set()
    for _, v in nodes.items():
        positions = positions | calculate_antinodes(v, l, w, False)
        posistion2 = posistion2 | calculate_antinodes(v, l, w, True)
    sum1 = len(positions)
    sum2 = len(posistion2)

       

    return f"{sum1}, {sum2}"
