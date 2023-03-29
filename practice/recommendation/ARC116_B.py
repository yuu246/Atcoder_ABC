N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
mod = 998244353
for i in range(N):
    ans += A[i] ** 2 % mod

tmp = 0
for i in range(N-2, -1, -1):
    tmp = (tmp*2 + A[i+1]) % mod
    ans += A[i] * tmp % mod
    ans %= mod

print(ans)
