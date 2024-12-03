import re

def sum_multiplications(s):
    pattern = r"mul\((\d+),(\d+)\)" 
    
    matches = re.findall(pattern, s)
    
    total_sum = sum(int(n1) * int(n2) for n1, n2 in matches)
    
    return total_sum

def sum_multiplications2(s):
    new_list = s.split('do()')
    
    sum = 0
    for n in new_list:
        # print(n.split("don't()")[0])
        sum += sum_multiplications(n.split("don't()")[0])   
    return sum

def solve():
    sum = 0
    sum2 = 0
    with open("day3/input.txt", "r") as file:
        lines = file.read().split("\n")
        for l in lines:
            sum += sum_multiplications(l)
            sum2 += sum_multiplications2(l)
    return f"{sum}, {sum2}"
    
        