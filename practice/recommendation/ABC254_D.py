N = int(input())

cnt = [0 for i in range(N+1)]

for i in range(1, N+1):
    val = i
    d = 2
    while d * d <= val:
        if val % (d * d) == 0:
            val //= (d*d)
        else:
            d += 1
    cnt[val] += 1

ans = 0
for c in cnt:
    ans += c*c
print(ans)
