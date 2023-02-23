N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
sum = [0]*(N+1)
for i in range(1, N+1):
    sum[i] = sum[i-1] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    ans = sum[R] - sum[L-1]
    print(ans)
