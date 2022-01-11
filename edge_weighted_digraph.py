# edge_weighted_digraph.py

class Edge:
    def __init__(self, v, w, wt):
        self.hd = v
        self.tl = w
        self.wt = wt

    def head(self):
        return self.hd

    def tail(self):
        return self.tl

    def weight(self):
        return self.wt

    def __repr__(self):
        return f'Edge({self.hd}, {self.tl}, {self.wt})'

    def __str__(self):
        return f'{self.hd}->{self.tl} {self.wt:.2f}'


class EdgeWeightedDigraph:
    def __init__(self, n):
        self.V, self.E = n, 0
        self.adj = [[] for v in range(self.V)]

    def add(self, e):
        self.adj[e.head()].append(e)
        self.E += 1

    def add_edge(self, v, w, wt):
        self.add(Edge(v, w, wt))

    def edges(self):
        for v in range(self.V):
            for e in self.adj[v]:
                yield e

    def edge_list(self):
        return list(self.edges())

    def __repr__(self):
        lines = [None for _ in range(g.E + 1)]

        lines[0] = f'{self.V} vertices, {self.E} edges'

        for count, e in enumerate(self.edges()):
            lines[count + 1] = str(e)

        return '\n'.join(lines)


if __name__ == '__main__':
    V = 8
    EDGES = [
        Edge(4, 5, 0.35), Edge(5, 4, 0.35), Edge(4, 7, 0.37), Edge(5, 7, 0.28),
        Edge(7, 5, 0.28), Edge(5, 1, 0.32), Edge(0, 4, 0.38), Edge(0, 2, 0.26),
        Edge(7, 3, 0.39), Edge(1, 3, 0.29), Edge(2, 7, 0.34), Edge(6, 2, 0.40),
        Edge(3, 6, 0.52), Edge(6, 0, 0.58), Edge(6, 4, 0.93)
        ]

    g = EdgeWeightedDigraph(V)

    for e in EDGES:
        g.add(e)
