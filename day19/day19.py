def is_allowed(allowed, combo):
    global all_combos
    if len(combo) == 0:
        return 1
    if combo in all_combos:
        return all_combos[combo]
    sum = 0
    for item in allowed:
        length = len(item)
        if combo[0:length] == item:
            output = is_allowed(allowed, combo[length:])
            all_combos[combo[length:]] = output
            sum += output

    return sum
def solve():
    global all_combos
    sum1 = 0  
    sum2 = 0
    allowed = []
    with open("day19/input.txt", "r") as file:
        allowed, combos = file.read().split("\n\n")
        allowed = allowed.split(", ")
        combos = combos.split("\n")
    sum1 = 0
    all_combos = dict()
    for i,combo in enumerate(combos):
        # print(i)
        output = is_allowed(allowed, combo)
        sum1 += 1 if output > 0 else 0
        sum2 += output
    return f"Sum 1: {sum1}\nSum 2: {sum2}"

