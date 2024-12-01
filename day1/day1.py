
def solve():
    list1 = []
    list2 = []   
    data = {}
   
    with open("day1/input.txt", "r") as file:
        lines = file.read().split("\n")
        for l in lines:
            temp = l.split("   ")
            val1 = int(temp[0])
            val2 = int(temp[1])
            list1.append(int(temp[0]))
            list2.append(int(temp[1]))
            if(val2 in data):
                data[val2] += 1
            else:
                data[val2] = 1
    list1.sort()
    list2.sort()
    sum = 0
    sum2 = 0
    for i, value in enumerate(list1):
        if value  in data:
            sum2 += value * data[value]
        sum += abs(value - list2[i])
    return f"Part 1: {sum}\nPart 2: {sum2}"


# print(solve())