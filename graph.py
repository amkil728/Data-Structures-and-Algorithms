# graph.py

import sys

class Graph:
    def __init__(self, n):
        self.V = n
        self.M = 0
        self.vertices = list(range(n))
        self.adj = [[] for _ in range(n)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.M += 1

    def remove_edge(self, v, w):
        self.adj[v].remove(w)
        self.adj[w].remove(v)
        self.M -= 1

    def adjacent_vertices(self, v):
        return self.adj[v]

    def adjacent(self, v, w):
        for k in self.adj[v]:
            if k == w:
                return True

        return False

class DFS:
    def __init__(self, g, s):
        self.marked = [False for _ in range(g.V)]
        self.count = 0
        self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        self.count += 1
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)

class FindPathDFS:
    def __init__(self, g, s):
        self.source = s
        self.marked = [False for _ in range(g.V)]
        self.edge_to = [-1 for _ in range(g.V)]
        self.count = 0
        self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        self.count += 1
        
        for w in g.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(g, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        path = [v]

        while v != self.source:
            v = self.edge_to[v]
            path.append(v)

        path.reverse()

        return path


class FindPathBFS:
    def __init__(self, g, s):
        self.marked = [False for _ in range(g.V)]
        self.edge_to = [-1 for _ in range(g.V)]
        self.source = s
        self.bfs(g)

    def bfs(self, g):
        self.marked[self.source] = True
        to_visit = [self.source]

        while to_visit:
            curr = to_visit.pop(0)

            for w in g.adj[curr]:
                if not self.marked[w]:
                    to_visit.append(w)
                    self.marked[w] = True
                    self.edge_to[w] = curr

    def shortest_path_to(self, v):
        path = [v]

        while v != self.source:
            v = self.edge_to[v]
            path.append(v)

        path.reverse()

        return path


class ConnectedComponents:
    def __init__(self, g):
        self.id = [-1 for _ in range(g.V)]
        self.count = 0

        for s in range(g.V):
            if self.id[s] == -1:
                self.dfs(g, s)
                self.count += 1

        print(self.count)

    def dfs(self, g, v, indent=0):
        self.id[v] = self.count
        
        for w in g.adj[v]:
            if self.id[w] == -1:
                self.dfs(g, w)
            
    def connected(self, v, w):
        '''Checks if v and w are connected.'''
        return self.id[v] == self.id[w]


class Cycle:
    def __init__(self, g):
        self.marked = [False for _ in range(g.V)]
        self.edge_to = [-1 for _ in range(g.V)]
        self.cycle_start = -1

        for s in range(g.V):
            if not self.marked[s]:
                self.dfs(g, s, s)

    def dfs(self, g, u, v, indent=0):
        self.marked[v] = True

        print(indent * ' ' + 'visited', v)

        for w in g.adj[v]:
            print((indent + 2) * ' ' + 'checking', w)

            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(g, v, w, indent+2)
            elif w != u and self.cycle_start < 0:
                print(indent * ' ' + 'found a cycle', file=sys.stderr)
                self.cycle_start = w
                self.edge_to[w] = v

        print(indent * ' ' + 'done', v)

    def has_cycle(self):
        return self.cycle_start >= 0

    def cycle(self):
        if self.has_cycle():
            cycle = [self.cycle_start]

            curr = self.edge_to[self.cycle_start]

            while curr != self.cycle_start:
                cycle.append(curr)
                curr = self.edge_to[curr]

            cycle.append(self.cycle_start)

            return cycle


class Bipartite:
    def __init__(self, g):
        self.marked = [False for _ in range(g.V)]
        self.colour = [0 for _ in range(g.V)]
        self.colourable = True

        for s in range(g.V):
            if not self.marked[s]:
                self.dfs(g, s, 1)

    def dfs(self, g, v, c):
        self.marked[v] = True
        self.colour[v] = c

        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w, -c)
            elif self.colour[w] == c:
                self.colourable = False

def colour_graph(g, c1, c2):
    tc = Bipartite(g)

    if tc.colourable:
        print(c1 + ':', end=' ')

        for i, colour in enumerate(tc.colour):
            if colour == 1:
                print(i, end=' ')

        print()

        print(c2 + ':', end=' ')

        for i, colour in enumerate(tc.colour):
            if colour == -1:
                print(i, end=' ')

    else:
        print('not bipartite')


# V = 6, connected, cyclic
V1 = 6
E1 = [(0, 1), (0, 2), (0, 5), (1, 2),
      (2, 3), (2, 4), (3, 4), (3, 5)]

# V = 6, connected, acyclic (tree), bipartite
V2 = 6
E2 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]


# V = 10, 2 connected components, acyclic (forest), bipartite
V3 = 10
E3 = [(0, 1), (0, 2), (1, 3), (1, 4),
      (2, 5), (6, 7), (6, 8), (7, 9)]

# V = 10, 2 connected components, cyclic
# 1st component is tree, bipartite
# 2nd component is cyclic, not bipartite
V4 = 10
E4 = [(0, 1), (0, 2), (1, 3), (1, 4),
      (2, 5), (6, 7), (6, 8), (7, 9),
      (7, 8)]

# V = 13, 3 connected components, cyclic (tinyG)
V5 = 13
E5 = [
    (0, 5), (4, 3), (0, 1), (9, 12),
    (6, 4), (5, 4), (0, 2), (11, 12),
    (9, 10), (0, 6), (7, 8), (9, 11),
    (5, 3)
    ]

# V = 13, connected, bipartite, cyclic
V6 = 13
E6 = [
    (0, 1), (0, 2), (0, 5), (0, 6),
    (1, 3), (3, 5), (5, 4), (4, 6),
    (6, 7), (7, 8), (8, 10), (10, 9),
    (10, 12), (9, 11), (11, 12)
    ]


if __name__ == '__main__':
    g1 = Graph(V1)
    for v, w in E1:
        g1.add_edge(v, w)

    g2 = Graph(V2)
    for v, w in E2:
        g2.add_edge(v, w)

    g3 = Graph(V3)
    for v, w in E3:
        g3.add_edge(v, w)

    g4 = Graph(V4)
    for v, w in E4:
        g4.add_edge(v, w)

    tinyG = g5 = Graph(V5)
    for v, w in E5:
        g5.add_edge(v, w)

    g6 = Graph(V6)
    for v, w in E6:
        g6.add_edge(v, w)
