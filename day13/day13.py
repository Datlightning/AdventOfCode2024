
def solve_equation(equation,p2 = False):
    items = equation.split("\n")
    item1,item2,item3 = items
    e, f = item3.split(":")[1].split(",")
    e = int(e.split("=")[1])
    f = int(f.split("=")[1])
    a,c = item1.split(":")[1].split(",")
    a = int(a.split("+")[1])
    c = int(c.split("+")[1])
    b,d = item2.split(":")[1].split(",")
    b = int(b.split("+")[1])
    d = int(d.split("+")[1])
    if p2:
        e += 10000000000000
        f += 10000000000000
    
    dem = (a*d)-(c*b)
    assert dem != 0
    det1 = (e*d - b*f)/dem
    det2 = (a*f - e*c)/dem
    
    if(int(det1) == det1 and int(det2) == det2 and det1 >= 0 and det2 >= 0):
        return 3 * det1 + det2
    return 0


def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    
    with open("day13/input.txt", "r") as file:
        g =  [i for i in file.read().split("\n\n")]
    for item in g:

        sum1 += (solve_equation(item))
        sum2 += (solve_equation(item, True))


    return f"{sum1}, {sum2}"

