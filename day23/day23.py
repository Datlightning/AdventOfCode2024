from functools import lru_cache
from itertools import combinations
import networkx as nx





def solve(real_input = True):
    sum1 = 0  
    sum2 = 0
    connections_data = {}
    G = nx.Graph()
   
    with open("day23/input.txt" if real_input else "day23/sample_input.txt", "r") as file:
        connections = file.read().split("\n")
    sum1 = 0
    important_nodes = set()
    edges = []
    for connection in connections:
        c1, c2 = connection.split("-")
        if c1 not in connections_data:
            connections_data[c1] = [c2]
        else:
            connections_data[c1].append(c2)
        if c2 not in connections_data:
            connections_data[c2] = [c1]
        else:
            connections_data[c2].append(c1)
        if c2[0] == "t":
            important_nodes.add(c2)
        if c1[0] == 't':
            important_nodes.add(c1)
        edges.append((c1,c2))


 
    for u, v, w in combinations(connections_data.keys(), 3):
        if u not in important_nodes and v not in important_nodes and w not in important_nodes:
            continue
        if v in connections_data[u] and w in connections_data[v] and w in connections_data[u]:
            sum1 += 1
    G.add_edges_from(edges)
    cliques = list(nx.find_cliques(G))
    sum2 = ",".join(sorted(max(cliques, key = len)))

    return f"Part 1: {sum1}\nPart 2: {sum2}"
if __name__ == "__main__":
    print(solve(False))