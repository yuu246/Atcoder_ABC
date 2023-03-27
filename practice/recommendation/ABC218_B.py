P = list(map(int, input().split()))
ans = ''
for x in P:
    ans += chr(x+64).lower()

print(ans)
