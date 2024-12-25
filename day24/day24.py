from functools import lru_cache
from itertools import combinations
from collections import deque
from graphviz import CalledProcessError, Graph
import networkx as nx
from random import randint


def solve(real_input = True):
    part1 = 0  
    part2 = 0
    inputs = {}
    instructions = {}
    with open("day24/input.txt" if real_input else "day24/sample_input.txt", "r") as file:
        inputs, instructions = file.read().split("\n\n")
    part1 = 0
    inputs = inputs.split("\n")
    instructions = instructions.split("\n")
    bits = {}
    bits2 = {}
    target_sum = 0
    Y = []
    X = []
    for i in inputs:
        k,v = i.split(": ")
        if k[0] == "x":
            X.append(k)
        elif k[0] == "y":
            Y.append(k)
        bits[k] = v
        bits2[k] = v
    X = sorted(X, reverse=True)
    Y = sorted(Y, reverse=True)
    X_BINARY = [str(bits[x]) for x in X]
    Y_BINARY = [str(bits[y]) for y in Y]
    target_sum = bin(int("".join(X_BINARY),2) + int("".join(Y_BINARY),2))
    Q = deque([])
    dot = Graph()
    G = nx.Graph()
    gates = {}
   
    for i in instructions:
        n1, ins, n2, _ , n3 = i.split(" ")
        gates[n3] = [n1,ins,n2]
        Q.append((n1, ins, n2, n3))
        
    try:  
        dot.render('day24/graph')
    except CalledProcessError:
        print("close the tab")

    # try:
    # except CalledProcessError:
    #     print('Delete "graph.pdf" from "day25" for a visualization.')
    while Q:
        n1, ins, n2, n3 = Q.popleft()
        if n1 in bits and n2 in bits:
            v1, v2 = int(bits[n1]), int(bits[n2])
            if ins == "XOR":
                bits[n3] = 1 if v1 != v2 else 0
            elif ins == "AND":
                bits[n3] = 1 if v1 == v2 == 1 else 0
            else:
                assert ins == "OR", f"Insert: {ins}" 
                bits[n3] = 1 if v1 == 1 or v2 == 1 else 0
        else:
            Q.append((n1, ins, n2, n3))
    
    Z = []
    
    for k,v in bits.items():
        if k[0] == "z":
            Z.append(k)
    Z = sorted(Z, reverse=True)
    S = ""

    for i in Z:
        S += str(bits[i])
    part1 = int(S,2)

    
    
    swap = [("z08", "mvb"), ("rds", "jss"), ("z18", "wss"), ("z23", "bmn")]

    dot = Graph()

    for n1, n2 in swap:
        save = gates[n1]
        gates[n1] = gates[n2]
        gates[n2] = save
    
    for n3,v in gates.items():
        n1, ins, n2 = v
        G.add_edge(n3, n1)
        G.add_edge(n3, n2)
# Draw the graph
        dot.node(n3)
        dot.node(n2)
        dot.node(n1)
        dot.edge(n2, n3, label = ins)
        dot.edge(n1, n3, label = ins)
        Q.append((n1, ins, n2, n3))
    try:  
        dot.render('day24/graph')
    except CalledProcessError:
        print("close the tab")
    while False:
        bits2 = {}
        for i in inputs:
            k,_ = i.split(": ")
            bits2[k] = randint(0,1)
        X_BINARY = [str(bits2[x]) for x in X]
        Y_BINARY = [str(bits2[y]) for y in Y]
        target_sum = bin(int("".join(X_BINARY),2) + int("".join(Y_BINARY),2))
        Q = deque([])
    
        for n3,v in gates.items():
            n1, ins, n2 = v
            Q.append((n1, ins, n2, n3))
        while Q:
            n1, ins, n2, n3 = Q.popleft()
            if n1 in bits2 and n2 in bits2:
                v1, v2 = int(bits2[n1]), int(bits2[n2])
                if ins == "XOR":
                    bits2[n3] = 1 if v1 != v2 else 0
                elif ins == "AND":
                    bits2[n3] = 1 if v1 == v2 == 1 else 0
                else:
                    assert ins == "OR", f"Insert: {ins}" 
                    bits2[n3] = 1 if v1 == 1 or v2 == 1 else 0
            else:
                Q.append((n1, ins, n2, n3))
    
        S = ""
        Z = sorted(Z, reverse=False)
        for i in Z:
            S += str(bits2[i])
        
 
        target_sum = target_sum[2:][::-1]
        # print(target_sum)
        # print(S)
        wrong = []
        for i,v in enumerate(target_sum):  
            if i == 0:
                pass
            if v != S[i]:
                zvalue = "z" + str(i) if len(str(i)) == 2 else "0" + str(i)        
                assert str(bits2[zvalue]) == str(S[i]), f"Length of current: {len(S)}"
                wrong.append(zvalue)
                # print(f"{zvalue} is at index {i} and is {bits2[zvalue]} or {S[i]} but should be {v}")
        print(wrong)
    answers = []
    for pair in swap:
        v1, v2 = pair
        answers.append(v1)
        answers.append(v2)
    part2 = ",".join(sorted(answers))

    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve(True))