class BIT:
    def __init__(self, n) -> None:
        self.size = n
        self.tree = [0 for i in range(n+1)]

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total
