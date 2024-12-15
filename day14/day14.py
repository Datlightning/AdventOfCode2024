def calculate_position(n, start, direction,w,h):
    x,y =start
    dx,dy = direction
    y += dy * n
    x += dx * n
    y %= h
    x %= w
    mx = w//2
    my = h//2
    # print((y,x))
    if x < mx and y < my:
        return 1, (y,x)
    elif x > mx and y < my:
        return 2, (y,x)
    elif x < mx  and y > my:
        return 3, (y,x)
    elif x > mx and y > my:
        return 4, (y,x)
    return 0, (y,x)
def mul(list):
    if not list:
        return 1
    
    return list[0] * mul(list[1:] )
def generate_string(n, w, h, current):
    output = str(n)
    for y in range(h):
        string = ""
        for x in range(w):
            if (y,x) in current:
                string += "#"
            else:
                string += "."
        output+="\n" + string
    return output
def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    
    with open("day14/input.txt", "r") as file:
        g =  [i for i in file.read().split("\n")]
    for i, values in enumerate(g):
        g[i] = values.split(" ")
        g[i][0] = list(map(int, g[i][0].split("=")[1].split(",")))
        g[i][1] = list(map(int, g[i][1].split("=")[1].split(",")))
    n = 100
    w = 101
    h = 103
    output = [0,0,0,0,0]
   
    for n in range(100000):
        current = set()
        for i in g:

            # print(i)
                quad, temp = calculate_position(n, i[0], i[1], w,h)
                if(temp in current and not n == 100):
                    break
                current.add(temp)
                
                if(n == 100):
                    output[quad] += 1
        else:   
                if( n == 100):
                    continue
                sum2 = n
                print(sum2)
                break
    sum1 = mul(output[1:])


    return f"{sum1}, {generate_string(n, w,h,current)}"

