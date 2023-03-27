A, B, C, X, Y = map(int, input().split())

ans = 10 ** 19
Z = max(X, Y)
for i in range(0, 2*Z+1):
    money = 0
    money += C*i
    if X - (i/2) > 0:
        money += A*(X-(i/2))
    if Y - (i/2) > 0:
        money += B*(Y-(i/2))
    ans = min(ans, money)
print(int(ans))
