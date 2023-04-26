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



H,W = map(int,input().split())
Q = int(input())
query = [list(map(int,input().split())) for _ in range(Q)]

uf = UnionFind(H*W)
G = [[0]*W for _ in range(H)]
for q in query:
    if q[0] == 1:
        r,c = q[1:]
        r,c = r-1,c-1

        G[r][c] = 1
        d = [(-1,0), (0,1), (1,0), (0,-1)]
        for i,j in d:
            if (0 <= r+i < H) and (0 <= c+j < W) and G[r+i][c+j] == 1:
                uf.union(W*r+c, W*(r+i)+(c+j))

    else:
        ra,ca,rb,cb = q[1:]
        ra,ca,rb,cb = ra-1,ca-1,rb-1,cb-1

        if (ra,ca) == (rb,cb):
            if G[ra][ca] == 1:  print('Yes')
            else:   print('No')
        else:
            if uf.same(W*ra+ca, W*rb+cb):   print('Yes')
            else:   print('No')

    # print(*G, sep='\n')
