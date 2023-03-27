x, y = 0, 0
for i in range(3):
    x1, y1 = map(int, input().split())
    x = x ^ x1
    y = y ^ y1
print(x, y)
