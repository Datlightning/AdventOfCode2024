from functools import lru_cache
from itertools import combinations
from collections import deque
from graphviz import CalledProcessError, Graph
import networkx as nx
from random import randint

def display(output):
    for n in output:
        print(n)

def valid_key(key, lock):
    for y in range(len(key)):
        for x in range(len(key[0])):
            if key[y][x] == "#" and lock[y][x] == "#":
                return 0
    return 1
   
def solve(real_input = True):
    part1 = 0  
    part2 = 0
    inputs = {}
  
    
    with open("day25/input.txt" if real_input else "day25/sample_input.txt", "r") as file:
        inputs = file.read().split("\n\n")
    for k,i in enumerate(inputs):
        for i2 in inputs[k:]:
            part1 += valid_key(i, i2)
  

    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve(False))