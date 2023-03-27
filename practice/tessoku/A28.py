N = int(input())
ans = 0

for i in range(N):
    T, A = input().split()
    if T == '+':
        ans += int(A)
    elif T == '-':
        ans -= int(A)
    elif T == '*':
        ans *= int(A)
    if ans < 0:
        ans += 10000
    ans = ans % 10000
    print(ans)
