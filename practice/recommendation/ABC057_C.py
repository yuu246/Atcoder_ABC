import math
N = int(input())
base = int(math.sqrt(N))

for x in range(base, 0, -1):
    if N % x == 0:
        A = x
        break
B = N // A
ans = 1
while B > 9:
    ans += 1
    B //= 10

print(ans)
