from collections import Counter
N, P = map(int, input().split())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


lst = prime_factorize(P)
cnt = Counter(lst)
key = list(cnt.keys())
ans = 1
for k in key:
    if cnt[k] >= N:
        kake = k ** (cnt[k] // N)
        ans *= kake
print(ans)
