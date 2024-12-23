from heapq import heappop, heappush
def display(walls, width, path = None):
    output=""
    for y in range(width):
        string = ""
        for x in range(width):
            if (y,x) in walls:
                string += "#"
            elif (y,x) in path:
                string += "O"
            else:
                string += "."
        output += string
        output += "\n"
        print(string)

    
    with open("output.txt","w") as file:
        file.write(str(output))
    
def djikstra(start, walls, height):
        q = [(0,*start,[])]
        DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
        seen = set()
        while q:
            # display(walls, height, path=seen)
            score, y, x, path = heappop(q)
            if (y,x) == (height-1, height-1):
                final_path = path
                # display(walls, height, path = path)
                return score, final_path
            if (y,x) in seen:
                continue
            seen.add((y,x))
            for dy,dx in DIRS:
                ny = y + dy
                nx = x + dx
                if 0<=nx<height and 0<=ny<height and (ny, nx) not in walls:
                    heappush(q, (score + 1, ny, nx, path + [(ny,nx)]))
        return -1, path
def solve():
    sum1 = 0  
    sum2 = 0

    points = []
    with open("day18/input.txt", "r") as file:
        points  =   file.read().split("\n")
        points = [(int(point.split(",")[1]), int(point.split(",")[0])) for point in points]
    height = 71
    memory = 1024
    
    walls = set()
    for i in range(memory):
        walls.add(points[i])
    sum1, path = djikstra((0,0), walls, height)
    for i,point in enumerate(points):
        if  point in walls:
            continue
        walls.add(point)
        sum, path = djikstra((0,0), walls, height)
        # display(walls, height, path)
        # input()
        if sum == -1:
            # print(i)
            sum2 = f"{point[1]},{point[0]}"
            break

        # walls.remove(point)

    # for i in points:
    #     if i in possible_points:
    #         sum2 = f"{i[1],i[0]}"
    #         break
    return f"Sum 1: {sum1}\nSum 2: {sum2}"

if __name__ == "__main__":
    print(solve())