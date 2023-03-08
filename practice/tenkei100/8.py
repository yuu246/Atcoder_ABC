N = int(input())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10**20

for i in A:
    for j in B:
        time = 0
        for k in range(N):
            time += abs(i - A[k]) + abs(A[k] - B[k]) + abs(B[k] - j)
        ans = min(ans, time)

print(ans)
