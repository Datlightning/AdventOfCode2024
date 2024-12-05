from functools import cmp_to_key
rule_dictionary = {}

def goofsort(x,y):
    global rule_dictionary
    y_before_x = x in rule_dictionary and y in rule_dictionary[x]
    x_before_y = y in rule_dictionary and x in rule_dictionary[y]
    if x_before_y:
        return 1
    if y_before_x:
        return -1
    return 0

def reorderList(rules, reversed_rules, line):
    return sorted(line, key=cmp_to_key(goofsort))[len(line)//2]
def isRuleVaild(rules, reversed_rules, line):
    seen = set()
    do_not_see = set()
    for pos,n in enumerate(line):
        seen.add(n)
        if n in do_not_see:
            return 0
        if n not in reversed_rules:
            continue

        if reversed_rules[n] <= seen:
            continue
        else:
            # print(rules[n])
            do_not_see = do_not_see.union(reversed_rules[n])
            
    # print(line)
    return line[len(line)//2]

def solve():
    global rule_dictionary
    sum = 0
    sum2 = 0
    reversed_rule_dictionary = {}
    with open("day5/input.txt", "r") as file:
        rules, lines = file.read().split("\n\n")
        rules = rules.split("\n")
        for r in rules:
            k,v = r.split("|")
            if(int(v) in reversed_rule_dictionary):
                reversed_rule_dictionary[int(v)].add(int(k))
            else:
                reversed_rule_dictionary[int(v)] = set([int(k)])
            if(int(k) in rule_dictionary):
                rule_dictionary[int(k)].add(int(v))
            else:
                rule_dictionary[int(k)] = set([int(v)])
        lines = lines.split("\n")
        for i, line in enumerate(lines):
            lines[i] = line.split(",")
            lines[i] = list(map(int, lines[i]))
            output = isRuleVaild(rule_dictionary,reversed_rule_dictionary, lines[i])
            if output == 0:
                sum2 += reorderList(rule_dictionary, reversed_rule_dictionary, lines[i])
            sum += output
    return f"{sum}, {sum2}"
    
        