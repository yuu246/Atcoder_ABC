def check(n, x):
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    ans += 1
    return ans


while True:
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    else:
        print(check(N, X))
