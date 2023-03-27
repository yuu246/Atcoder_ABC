# 入力など
n, r = map(int, input().split())
M = 1000000007


def to_bin(x):
    amari = []
    while x != 0:
        amari.append(x % 2)
        x = x // 2
    return amari


def power(a, b, M):
    ans = 1
    p = a
    bin_list = to_bin(b)
    for i in bin_list:
        if i == 1:
            ans = (ans * p) % M

        p = (p * p) % M
    return ans


# 手順 1：分子を求める
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

# 手順 2：分母を求める
b = 1
for i in range(1, r+1):
    b = (b * i) % M
for i in range(1, n-r+1):
    b = (b * i) % M


ans = (a * power(b, M-2, M)) % M
print(ans)
