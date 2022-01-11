# digraph_trace.py

import sys

class Digraph:
    def __init__(self, n):
        self.V = n
        self.M = 0
        self.adj = [list() for _ in range(n)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.M += 1

    def reverse(self):
        rev = Digraph(self.V)

        for v in range(self.V):
            for w in self.adj[v]:
                rev.add_edge(w, v)

        return rev

class DirectedDFS:
    def __init__(self, g, source):
        self.marked = [False for _ in range(g.V)]

        try:
            for s in source:
                self.dfs(g, s)
        except:
            self.dfs(g, source)

    def dfs(self, g, v):
        self.marked[v] = True

        for w in g.adj[v]:
            if not self.is_marked(w):
                self.dfs(g, w)

    def is_marked(self, v):
        return self.marked[v]


class DirectedBFS:
    def __init__(self, g, source):
        self.marked = [False for _ in range(g.V)]

        try:
            for s in source:
                self.bfs(g, s)
        except:
            self.bfs(g, source)

    def bfs(self,  g, s):
        to_visit = [s]
        self.marked[s] = True

        while to_visit:
            curr = to_visit.pop(0)

            for v in g.adj[curr]:
                if not self.is_marked(v):
                    self.marked[v] = True
                    to_visit.append(v)

    def is_marked(self, v):
        return self.marked[v]

    def reachable(self):
        t = list()

        for v, mark in enumerate(self.marked):
            if mark:
                t.append(v)

        return t

class DirectedPathDFS():
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


class DirectedPathBFS:
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

    def has_path_to(self, v):
        return self.marked[v]

    def shortest_path_to(self, v):
        path = [v]

        while v != self.source:
            v = self.edge_to[v]
            path.append(v)

        path.reverse()

        return path


class DirectedCycle:
    def __init__(self, g):
        self.on_path = [False for _ in range(g.V)]
        self.edge_to = [-1 for _ in range(g.V)]
        self.marked = [False for _ in range(g.V)]
        self.cycle = None

        for v in range(g.V):
            if not self.marked[v]:
                self.dfs(g, v)

    def dfs(self, g, v, indent=0):
        if self.has_cycle():
            return
        
        self.marked[v] = True
        self.on_path[v] = True

        print(indent * ' ' + 'visiting',  v)

        for w in g.adj[v]:
            if self.has_cycle():
                return

            print((indent + 2) * ' ' + 'checking', w)

            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(g, w, indent+2)
            elif self.on_path[w]:
                print((indent + 2) * ' ' + 'found a cycle')
                self.cycle = [w]

                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]

                self.cycle.append(w)
                self.cycle.reverse()

            self.on_path[w] = False

    def has_cycle(self):
        return self.cycle is not None


class DepthFirstOrder:
    def __init__(self, g, s):
        self.marked = [False for _ in range(g.V)]
        self.pre = list()
        self.post = list()

        self.dfs(g, s)

        self.reverse_post = reversed(self.post[:])

    def dfs(self, g, v, indent=0):
        self.marked[v] = True

        print(' ' * indent + 'visiting', v)

        self.pre.append(v)

        for w in g.adj[v]:
            print(' ' * (indent + 2) + 'checking', w)

            if not self.marked[w]:
                self.dfs(g, w, indent + 2)

        print(' ' * indent + 'done', v)

        self.post.append(v)

# directed cycle
V1 = 13
edges1 = [
    (4, 2), (2, 3), (3, 2), (6, 0),
    (0, 1), (2, 0), (11, 12), (12, 9),
    (9, 10), (9, 11), (8, 9), (10, 12),
    (11, 4), (4, 3), (3, 5), (7, 8),
    (8, 7), (5, 4), (0, 5), (6, 4),
    (6, 9), (7, 6)
    ]

# acyclic
V2 = 13
edges2 = [
    (0, 1), (0, 6), (0, 5), (2, 0),
    (2, 3), (3, 5), (5, 4), (6, 4),
    (6, 9), (7, 6), (8, 7), (9, 10),
    (9, 11), (9, 12), (11, 12)
    ]
    
    

if __name__ == '__main__':
    g1 = Digraph(V1)

    for v, w in edges1:
        g1.add_edge(v, w)

    g2 = Digraph(V2)

    for v, w in edges2:
        g2.add_edge(v, w)
