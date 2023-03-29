N, X = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] > X:
        ans += A[i] - X
        A[i] = X

for idx in range(N-1):
    if A[idx] + A[idx+1] > X:
        ans += A[idx] + A[idx+1] - X
        A[idx+1] = X - A[idx]

print(ans)
