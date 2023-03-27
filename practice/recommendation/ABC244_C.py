from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))


count = defaultdict(int)

for i in range(N):
    count[A[i]] += 1

ans = N * (N - 1) // 2

for x in count.values():
    ans -= x * (x - 1) // 2

print(ans)
