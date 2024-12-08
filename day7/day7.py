def is_valid(current, target, values, index, memo, p2 = False):
    if index == len(values) and current == target:
        return 1
    elif index == len(values):
        return 0
    elif current > target:
        return 0
    
    result = 0
    if current * values[index] <= target:
        result += is_valid(current * values[index], target, values, index + 1, memo, p2)
    if current + values[index] <= target:
        result += is_valid(current + values[index], target, values, index + 1, memo, p2)
    if p2:
        if int(str(current) + str(values[index])) <= target:
            # print(int(str(current) + str(values[index])))
            result += is_valid(int(str(current) + str(values[index])), target, values, index + 1, memo, p2)

    # memo[(current, index)] = result
    return result

def solve():
    sum1 = 0  
    sum2 = 0
    equations = []
    with open("day7/input.txt", "r") as file:
        equations = file.read().split("\n")
        for i, v in enumerate(equations):
            equations[i] = v.split(":")

    for current, values in equations:
        current = int(current)
        values = list(map(int, values.strip().split(" ")))
       
        memo = {}
        if is_valid(values[0], current, values, 1, memo) > 0:
            sum1 += current
        if is_valid(values[0], current, values, 1, memo, True) > 0:
            sum2 += current

    return f"{sum1}, {sum2}"
