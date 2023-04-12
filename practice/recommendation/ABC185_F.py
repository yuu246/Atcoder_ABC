class BIT:
    def __init__(self, n) -> None:
        self.size = n
        self.tree = [0 for i in range(n+1)]

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] ^= x
            i += i & -i

    def sum(self, i):
        total = 0
        while i > 0:
            total ^= self.tree[i]
            i -= i & -i
        return total


N, Q = map(int, input().split())
bit = BIT(N)
A = list(map(int, input().split()))
for i in range(N):
    bit.add(i+1, A[i])

for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        bit.add(x, y)
    else:
        ans = bit.sum(y) ^ bit.sum(x-1)
        print(ans)
