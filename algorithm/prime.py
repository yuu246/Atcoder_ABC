# エラストネスの篩 O(NlogN)
def prime_serch(N):
    isprime = [True] * (N+1)

    isprime[0], isprime[1] = False, False

    for x in range(2, N+1):
        if not isprime[x]:
            continue
        q = x + x
        while q <= N:
            isprime[q] = False
            q += x
    return isprime
