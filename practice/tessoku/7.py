def isprime(N):
    Limit = int(N**0.5)
    for i in range(2, Limit+1):
        if N % i == 0:
            return False
    return True


Q = int(input())

for _ in range(Q):
    x = int(input())
    ans = isprime(x)
    if ans:
        print('Yes')
    else:
        print('No')
