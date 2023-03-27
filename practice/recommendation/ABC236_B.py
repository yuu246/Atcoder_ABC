N = int(input())
A = list(map(int, input().split()))
ans = 0
for x in A:
    ans = ans ^ x
print(ans)
