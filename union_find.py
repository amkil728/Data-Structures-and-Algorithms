# union_find.py

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.roots = [i for i in range(n)]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        raise NotImplementedError

    def union(self, p, q):
        raise NotImplementedError


class QuickFind(UnionFind):
    def find(self, p):
        return self.roots[p]

    def union(self, p, q):
        p_root, q_root = self.roots[p], self.roots[q]
        
        for i, root in enumerate(self.roots):
            if root == p_root:
                self.roots[i] = self.roots[q]
                self.count -= 1

class QuickUnion(UnionFind):
    def find(self, p):
        while self.roots[p] != p:
            p = self.roots[p]

        return p

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)

        if p_root != q_root:
            self.roots[p_root] = q_root
            self.count -= 1

if __name__ == '__main__':
    pairs = [
        (4,3), (3,8), (6,5), (9,4), (2,1), (8,9),
        (5,0), (7,2), (6,1), (1,0), (6,7)
	]

    uf = QuickUnion(10)

    for p, q in pairs:
        if not uf.connected(p, q):
            uf.union(p, q)
            print(p, q)

    print('Number of components:', uf.count)
