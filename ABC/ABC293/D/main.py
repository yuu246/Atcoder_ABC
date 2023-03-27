#!/usr/bin/env python3
class UnionFind():

    '''
    @param par 要素の親頂点の番号 (自身が根の場合は -1)
    @param size 要素 x の属する根付き木に含まれる頂点数
    @param rank 要素 x の属する根付き木の高さ
    '''

    def __init__(self, N) -> None:
        self.par = [-1 for n in range(N)]
        self.size = [-1 for n in range(N)]
        self.rank = [0 for n in range(N)]

    # 要素の根を返す
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # グループが同じかの判断をする
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    # ２つのグループを結合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.size[rx] += self.size[ry]
        return True

    # ｘが属する木のサイズを返す
    def size(self, x):
        return self.size(self.root(x))


N, M = map(int, input().split())

uf = UnionFind(N+1)
ans = 0
for _ in range(M):
    sousa = list(input().split())
    A = int(sousa[0])
    B = int(sousa[2])
    if uf.is_same(A, B):
        ans += 1
    uf.unite(A, B)

size = 0
for i in range(1, N+1):
    if i == uf.root(i):
        size += 1
Y = size - ans
print(f'{ans} {Y}')
