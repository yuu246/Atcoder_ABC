X = int(input())
n = 1
while True:
    if n*(n+1) >= 2*X:
        break
    else:
        n += 1

print(n)
