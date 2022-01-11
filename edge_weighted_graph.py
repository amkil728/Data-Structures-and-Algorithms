# edge_weighted_graph.py

from priority_queue import MinPriorityQueue

class Edge:
    def __init__(self, v, w, x):
        self.v = v
        self.w = w
        self.wt = x

    def weight(self):
        return self.wt

    def either(self):
        return self.v

    def other(self, vertex):
        return self.w if vertex == self.v else self.v

    def __eq__(self, other):
        v1, v2 = self.either(), other.either()
        w1, w2 = self.other(v1), other.other(v2)

        if v1 > w1:
            w1, v1 = v1, w1
        if v2 > w2:
            w2, v2 = v2, w2

        return v1 == v2 and w1 == w2 and self.weight() == other.weight()

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __repr__(self):
        return f'{self.v}-{self.w} {self.weight():.2f}'


class EdgeWeightedGraph:
    def __init__(self, n):
        self.V = n
        self.E = 0
        self.adj = [[] for v in range(n)]

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1

    def are_adjacent(self, v, w):
        for e in self.adjacent_edges(v):
            if e.other(v) == w:
                return True
        return False

    def adjacent_edges(self, v):
        return iter(self.adj[v])

    def edge_list(self):
        edges = [None for _ in range(self.E)]
        i = 0

        for v in range(self.V):
            for e in self.adjacent_edges(v):
                if e.other(v) > v:
                    edges[i] = e
                    i += 1

        return edges


    def edges(self):
        for v in range(self.V):
            for e in self.adjacent_edges(v):
                if e.other(v) > v:
                    yield e


    def __repr__(self):
        str_parts = [None for _ in range(self.E + 1)]

        str_parts[0] = f'{self.V} vertices, {self.E} edges'

        edge_count = 1

        for e in self.edges():
            str_parts[edge_count] = str(e)
            edge_count += 1

        return '\n'.join(str_parts)


class MST:
    def edges(self):
        '''returns an iterator of edges of the MST'''
        raise NotImplementedError

    def edge_list(self):
        '''returns a list of the edges of the MST'''
        raise NotImplementedError

    def weight(self):
        '''returns the weight of the MST'''
        raise NotImplementedError


class LazyPrimMST(MST):
    def __init__(self, g):
        self.marked = [False for v in range(g.V)]
        self.mst_edges = list()
        self.pq = MinPriorityQueue()
        self.wt = 0

        self.prim(g)


    def prim(self, g):
        self.visit(g, 0)

        while not self.pq.empty():
            curr_edge = self.pq.remove_min()
            
            v = curr_edge.either()
            w = curr_edge.other(v)

            if self.marked[v] and self.marked[w]:
                continue

            self.mst_edges.append(curr_edge)
            self.wt += curr_edge.weight()

            if self.marked[v]:
                self.visit(g, w)
            else:
                self.visit(g, v)


    def visit(self, g, v):
        self.marked[v] = True

        for e in g.adjacent_edges(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        for e in self.mst_edges:
            yield e

    def edge_list(self):
        return self.mst_edges

    def weight(self):
        return self.wt


class KruskalMST:
    def __init__(self, g):
        # parent vertex of v: initially, there are V single vertex trees
        self.parent = [v for v in range(g.V)]

        # if v is a root, self.size[v] is the size of the tree rooted at v
        self.size = [1 for v in range(g.V)]

        # mst is initially empty with 0 weight
        self.mst, self.wt = list(), 0

        # build PQ containing each edge
        edge_pq = MinPriorityQueue()

        for e in g.edges():
            edge_pq.insert(e)

        self.edge_pq = edge_pq

        # run Kruskal's algorithm
        self.kruskal(g)


    def kruskal(self, g):
        while not self.edge_pq.empty():
            # get current edge of minimum weight
            e = self.edge_pq.remove_min()

            v = e.either()
            w = e.other(v)

            # get root vertex for v and w
            i, j = self.find(v), self.find(w)

            # skip edge if both its vertices belong to the same tree
            if i == j:
                continue

            # otherwise, add edge to mst
            self.mst.append(e)

            # update MST weight
            self.wt += e.weight()

            # and add smaller tree to larger
            if self.size[i] < self.size[j]:
                self.size[j] += self.size[i]
                self.parent[i] = j
            else:
                self.size[i] += self.size[j]
                self.parent[j] = i

    def find(self, v):
        '''finds parent vertex of i: if i is a tree, returns i.'''
        w = self.parent[v]

        if v == w:
            return v
        else:
            self.parent[v] = self.find(w)
            return self.parent[v]

    def union(self, i, j):
        '''combines the trees rooted at i and j.'''
        if self.size[i] < self.size[j]:
            self.parent[i] = j
        else:
            self.parent[j] = i


    def edges(self):
        for e in self.mst:
            yield e

    def edge_list(self):
        return self.mst

    def weight(self):
        return self.wt


V = 8
EDGES = [
    Edge(4, 5, 0.35), Edge(4, 7, 0.37), Edge(5, 7, 0.28), Edge(0, 7, 0.16),
    Edge(1, 5, 0.32), Edge(0, 4, 0.38), Edge(2, 3, 0.17), Edge(1, 7, 0.19),
    Edge(0, 2, 0.26), Edge(1, 2, 0.36), Edge(1, 3, 0.29), Edge(2, 7, 0.34),
    Edge(6, 2, 0.40), Edge(3, 6, 0.52), Edge(6, 0, 0.58), Edge(6, 4, 0.93)
    ]

if __name__ == '__main__':
    g = EdgeWeightedGraph(V)

    for e in EDGES:
        g.add_edge(e)
