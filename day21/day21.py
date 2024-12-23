from heapq import heappush, heappop
from functools import lru_cache
from tracemalloc import start

path_conversion = {
    (1,0):"v",
    (-1,0):"^",
    (0,1):">",
    (0,-1):"<"
}
cache = {}
dpositions = {
        "#":(0,0),
        "^":(0,1),
        "A":(0,2),
        "<":(1,0),
        "v":(1,1),
        ">":(1,2)
    }
reversed_dpositions = {v:k for k,v in dpositions.items()}
npositions = {
        '7':(0,0),
        '8':(0,1),
        '9':(0,2),
        '4':(1,0),
        '5':(1,1),
        '6':(1,2),
        '1':(2,0),
        '2':(2,1),
        '3':(2,2),
        '0':(3,1),
        "A":(3,2),
        "#":(3,0)
    }
    
reversed_npositions = {v:k for k,v in npositions.items()}
@lru_cache(None)
def get_paths(start_character, end_character, keypad=True):
    positions = dpositions if keypad else npositions
    reversed_positions = reversed_dpositions if keypad else reversed_npositions
    sy,sx = positions[start_character]
    end = positions[end_character]

    q = [(0,0,sy,sx, 0,0, "")]
    seen  = dict()
    valid_paths = []
    low_score = 1<<60
    while q:
        _,score, y, x, pdy,pdx, path = heappop(q)
        if(y,x,pdy,pdx) in seen and score > seen[(y,x,pdy,pdx)]:
            continue
        seen[(y,x,pdy,pdx)] = score
        if len(path) + 1 > low_score:
            continue
        if (y,x) == end:
            valid_paths.append(path + "A")
            continue
        for dy, dx in [(0,1),(0,-1),(-1,0),(1,0)]:
            npoint = (y + dy, x + dx)
            if npoint in reversed_positions and reversed_positions[npoint] != "#":
                heappush(q, (score + 1 , score + 1, y + dy, x + dx, dy, dx, path + path_conversion[(dy,dx)]))
    return valid_paths

cost_cache = {}
@lru_cache(None)
def calculate_cost(a,b, keypad, depth = 0):
    if depth == 0:
        return min([len(x) for x in get_paths(a,b, True)])
    paths = get_paths(a,b, keypad)

    best_cost = 1<<60
    for path in paths:
        path = "A" + path
        cost = 0
        for i, a in enumerate(path[:-1], 1):
            b = path[i]
            cost += calculate_cost(a,b, True, depth - 1)
        best_cost = min(cost, best_cost)
    return best_cost

def solve(real_input = True):
    sum1 = 0  
    sum2 = 0
    combos = []
    
   
    with open("day21/input.txt" if real_input else "day21/sample_input.txt", "r") as file:
        combos =   file.read().split("\n")
    for combo in combos:
        output = "A" + combo 
        for pos, item in enumerate(output[:-1],1):
            sum1+= int(combo[:-1]) * calculate_cost(item, output[pos], False, 2)      
            sum2 += int(combo[:-1]) * calculate_cost(item, output[pos], False, 25)   
    #205160 is what we need in life
    
   
    return f"Sum 1: {sum1}\nSum 2: {sum2}"

if __name__ == "__main__":
    print(solve(False))