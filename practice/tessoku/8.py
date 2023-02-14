def power(a, b, m):
    binary = []
    while b > 1:
        amari = b % 2
        binary.append(amari)
        b = b // 2
        if b == 1:
            binary.append(1)
            break
    ans = 1
    p = a

    length = len(binary)

    for i in range(length):
        if binary[i]:
            ans = (ans * p) % m
        p = (p * p) % m

    return ans


a, b = map(int, input().split())
print(power(a, b, 1000000007))
