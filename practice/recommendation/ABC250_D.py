import math
N = int(input())
ue = N
ue = int(math.pow(ue, 1/3))
prime = list()


def is_prime(x):
    LIMIT = int(x ** 0.5)
    for i in range(2, LIMIT + 1):
        if x % i == 0:
            return False
    return True


for x in range(2, ue+1):
    if is_prime(x):
        prime.append(x)


idx = 0
ans = 0
for idx_p in range(len(prime)):
    p = prime[idx_p]
    idx = idx_p
    while True:
        idx += 1
        if idx >= len(prime):
            idx -= 1
            break
        q = prime[idx]
        if p * q**3 <= N:
            ans += 1
        else:
            idx -= 1
            break

print(ans)
