from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


N,M = map(int,input().split())
G = UnionFind(N)
for _ in range(M):
    u,v = map(int,input().split())
    G.union(u-1,v-1)

K = int(input())
xy = [list(map(int,input().split())) for _ in range(K)]

tree = [0]*N
for i in range(N):
    tree[i] = G.find(i)

S = set()
for x,y in xy:
    S.add((tree[x-1], tree[y-1]))


Q = int(input())
for _ in range(Q):
    p,q = map(int,input().split())
    p,q = p-1,q-1

    if ((tree[p],tree[q]) in S) or ((tree[q],tree[p]) in S):
        print('No')
    else:
        print('Yes')

# print(tree)
# print(S)
