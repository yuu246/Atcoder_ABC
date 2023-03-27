N = int(input())
A = [0] + list(map(int, input().split()))
X = int(input())
sum = [0 for i in range(N+1)]

for i in range(1, N+1):
    sum[i] = sum[i-1] + A[i]

ans = N * (X // sum[N])
now = X % sum[N]

for i in range(1, N+1):
    if sum[i] > now:
        ans += i
        break

print(ans)
