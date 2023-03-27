N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0 for i in range(N)]
for i in range(N):
    if i == 0:
        pass
    else:
        R[i] = R[i-1]
    while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
        R[i] += 1

ans = sum(R) - (N-1) * N // 2
print(ans)
