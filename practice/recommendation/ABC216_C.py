N = int(input())
ans = ''
while N != 0:
    if N % 2 == 0:
        N = N // 2
        ans += 'B'
    else:
        N = N - 1
        ans += 'A'

ans = ans[::-1]
print(ans)
