import math
N = int(input())
n = int(math.sqrt(N))
ans = 0
for i in range(n, 0, -1):
    if N % i == 0:
        ans = N // i
        break
counter = 0
while ans >= 10:
    counter += 1
    ans //= 10

print(counter+1)
