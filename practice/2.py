N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

R = [-1] * N
R[0] = 1
for i in range(1, N):
    R[i] = R[i-1]
    while R[i] < N and A[R[i]+1] - A[i] <= K:
        R[i] += 1

ans = 0
for i in range(1, N):
    ans += (R[i] - i)
print(ans)
