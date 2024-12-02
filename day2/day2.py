
def isListGood(d):
    if sorted(d) != d:
        if sorted(d, reverse=True) != d:
            return False
    for i, v in enumerate(d[:-1]):
        if(abs(int(v) - int(d[i+1])) > 3 or int(v) == int(d[i+1])):
            break
    else:
        return True 
    return False
def solve():
    data = []
    with open("day2/input.txt", "r") as file:
        lines = file.read().split("\n")
        for l in lines:
            data.append(list(map(int, l.split(" "))))


    sum = 0
    sum2 = 0
    for d in data:
        if isListGood(d):
            sum += 1
            sum2 += 1
            continue
        for i in range(len(d)):
            if isListGood(d[0:i] + d[i+1:]):
                sum2 += 1
                break
   
    
    return f"Part 1: {sum}\nPart 2: {sum2}"


# print(solve())