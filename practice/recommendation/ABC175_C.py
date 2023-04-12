X, K, D = map(int, input().split())
if X < 0:
    X *= -1
cnt = X // D + 1
if cnt > K:
    print(abs(X - K * D))
    exit()

minus = abs(X - D * cnt)
plus = abs(X - D*(cnt-1))
if (K-cnt) % 2 == 0:
    print(minus)
else:
    print(plus)
