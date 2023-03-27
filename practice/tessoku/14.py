
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)
        self.siz = [1]*(n+1)

    def find(self, x):
        '''
        集合を表す木の根を返す
        '''
        if self.root[x] == -1:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            rx, ry = rx, ry
        self.root[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]


if __name__ == '__main__':
    N, Q = map(int, input().split())
    un = UnionFind(N)
    for _ in range(Q):
        q, x, y = map(int, input().split())

        if q == 1:
            un.unite(x, y)
        if q == 2:
            if un.find(x) == un.find(y):
                print('Yes')
            else:
                print('No')
