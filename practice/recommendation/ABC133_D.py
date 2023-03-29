N = int(input())

A = [0] + list(map(int, input().split()))

m1 = 0
for i in range(1, N+1):
    if i % 2 == 1:
        m1 += A[i]
    else:
        m1 -= A[i]
ans = [0 for i in range(N+1)]
ans[1] = m1
for i in range(1, N):
    ans[i+1] = (A[i] - (ans[i]//2))*2

print(*ans[1:])
