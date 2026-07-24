import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(n, edges):
    edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    mst = []
    cost = 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == n - 1:
                break
    return mst, cost


def prim(n, adj, start=0):
    INF = float("inf")
    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n
    key[start] = 0
    pq = [(0, start)]
    mst = []
    cost = 0
    while pq:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w
        for v, wt in adj[u]:
            if not in_mst[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))
    return mst, cost


n = 7
edges = [
    (0, 1, 7),
    (0, 3, 5),
    (1, 2, 8),
    (1, 3, 9),
    (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15),
    (3, 5, 6),
    (4, 5, 8),
    (4, 6, 9),
    (5, 6, 11),
]

adj = {i: [] for i in range(n)}
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

k_mst, k_cost = kruskal(n, edges[:])
p_mst, p_cost = prim(n, adj)

print("=== Kruskal's MST ===")
for u, v, w in k_mst:
    print(f"  Edge ({u} - {v}) Weight: {w}")
print(f"  Total MST Cost: {k_cost}")

print("\n=== Prim's MST ===")
for u, v, w in p_mst:
    print(f"  Edge ({u} - {v}) Weight: {w}")
print(f"  Total MST Cost: {p_cost}")
