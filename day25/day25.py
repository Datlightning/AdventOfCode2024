from functools import lru_cache
from itertools import combinations
from collections import deque
from graphviz import CalledProcessError, Graph
import networkx as nx
from random import randint

def display(output):
    for n in output:
        print(n)
h = 6 
def valid_key(key, lock):
    for i,v in enumerate(key):
        l = lock[i]
        if v + l > 5:
            return False
    return True
def solve(real_input = True):
    part1 = 0  
    part2 = 0
    inputs = {}
    keys = []
    locks = []
    
    with open("day25/input.txt" if real_input else "day25/sample_input.txt", "r") as file:
        inputs = file.read().split("\n\n")
    for i in inputs:
        i_grid = i.split("\n")
        if i_grid[0][0] == "#":
            heights = []
            for x in range(len(i_grid[0])):
                for y in range(len(i_grid)):
                    if i_grid[y][x] != "#":
                        heights.append(y - 1)
                        break
            locks.append(heights)
            
        if i_grid[h][0] == "#":
            heights = []
            for x in range(len(i_grid[0])):
                for y in reversed(range(len(i_grid))):
                    if i_grid[y][x] != "#":
                        heights.append(len(i_grid) - y - 2)
                        break

            keys.append(heights)
    
    for k in keys:
        for l in locks:
            part1 += 1 if valid_key(k,l) else 0
                

    return f"Part 1: {part1}\nPart 2: {part2}"
if __name__ == "__main__":
    print(solve(False))