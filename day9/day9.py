def replace_matching_dots(original_list, new_sublist):
    for i,v in enumerate(original_list):
        if v == ".":
            original_list[i:i + len(new_sublist)] = new_sublist
            break

    return original_list
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]

def sum_line(line, p2 = False):
    pointer = 0
    sum = 0
    while pointer < len(line):
        if(line[pointer] == "."):
            if(p2):
                pointer += 1
                continue
            v = line.pop()
            while v == ".":
                v = line.pop()
            sum += pointer * v
        else:
            sum += pointer * int(line[pointer])
        pointer += 1
    return sum

def solve():
    sum1 = 0  
    sum2 = 0
    g = []
    new_list = []
    new_list2 = []
    with open("day9/input.txt", "r") as file:
        g =  list(map(int, list(file.read().split("\n")[0])))
    pos = 0
    for i,v in enumerate(g):
        new_list.extend([pos if i % 2 == 0 else "." for _ in range(v)])
        new_list2.append([pos if i % 2 == 0 else "." for _ in range(v)])
        pos += i%2 
    
    data = {}
    for i,v in enumerate(new_list2):
        if "." not in v:
            continue
        data[i] = len(v)
       
    # print(data)

    pointer = len(new_list2) - 1
    while pointer > -1:

        current = new_list2[pointer]
        pointer -= 1

        if not current or "." in current:
            continue
        for key in sorted(data):
            if key > pointer:
                break
            value = data[key]
            if value >= len(current):
                remaining = value - len(current)
                data[key] = remaining
                new_list2[key] = replace_matching_dots(new_list2[key], current)
                new_list2[pointer + 1] = ["." for _ in range(len(current))]
                # print("".join(list(map(str,flatten_list(new_list2)))))
                break

        


    new_list3 = flatten_list(new_list2)
    sum2 = sum_line(new_list3, True)
    sum1 = sum_line(new_list)
    

    return f"{sum1}, {sum2}"
