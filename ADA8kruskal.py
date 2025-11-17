class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.padre[rb] = ra
            return True
        return False
def kruskal(n, aristas):
    aristas.sort(key=lambda x: x[2])  # Ordenar por peso
    uf = UnionFind(n)
    mst = []
    for u, v, peso in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))
    return mst
aristas = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]

print("Kruskal MST:")
print(kruskal(6, aristas))