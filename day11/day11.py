import math
from collections import defaultdict

def count_divisions_by_two(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count
def split_number_optimally(num):
    num_digits = math.floor(math.log10(num)) + 1
    
    half_digits = num_digits // 2
    
    divisor = 10 ** half_digits
    
    first_half = num // divisor
    second_half = num % divisor
    
    return (first_half, second_half)
def get_children(blinks, n, memo):
    if blinks == 0:
        return 1
    sum = 0
    if ((blinks, n) in memo):
        return memo[(blinks,n)]
    if n == 0:
        temp = get_children(blinks - 1, 1, memo)
        memo[(blinks - 1, 1)] = temp
        sum += temp
    elif (math.floor(math.log10(n)) + 1) % 2 == 0:
        n1, n2 = split_number_optimally(n)
        temp1 = get_children(blinks - 1, n1, memo)
        temp2 = get_children(blinks - 1, n2, memo)
        memo[(blinks-1, n1)] = temp1
        memo[(blinks-1, n2)] = temp2
        sum += temp1
        sum += temp2
    else:
        temp = get_children(blinks - 1, n * 2024, memo)
        memo[(blinks-1, n * 2024)] = temp
        sum += temp
    return sum


def blink(input):
    output = []
    for i in input:
        if i == 0:
            output.append(1)
        elif (math.floor(math.log10(i)) + 1) % 2 == 0:
            output.extend(split_number_optimally(i))
        else:
            output.append(i * 2024)          
    return output
def better_blink(data):
    for k,v in data.items():
        if k == 0:
            data[1] += v
            data[k] = 0
        if k == 2:
            print(k)
            for k2, v2 in data[2].items():
                if k2 > 1:
                    assert k2//2 == k2/2
                    data[2][k2//2] += 2 * v2
                else:
                    data[1] += 2 * v2
                data[2][k2] -= v2
    return data
def solve():
    sum1 = 0  
    sum2 = 0
    g = []
   
    with open("day11/input.txt", "r") as file:
        g =  list(map(int, file.read().split("\n")[0].split(" ")))
    memo = {}
    for i in g:
        sum1 += get_children(25, i, memo)
        sum2 += get_children(75, i, memo)
  
    # for i in range(50):
    #     print(i)
    #     g = blink(g)
    # sum2 = len(g)
   

    return f"{sum1}, {sum2}"

