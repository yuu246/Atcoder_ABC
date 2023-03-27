a, b = map(int, input().split())

y = [1, 2, 4, 5, 10, 20, 25, 50, 100]

ans = False
for i in range(a, b+1):
    if i in y:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
