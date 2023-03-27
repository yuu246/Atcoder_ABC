a, b = map(int, input().split())

m = 1000000007


def to_bin(x):
    amari = []
    while x != 0:
        amari.append(x % 2)
        x = x // 2
    return amari


ans = 1
p = a
bin_list = to_bin(b)
for i in bin_list:
    if i == 1:
        ans = (ans * p) % m

    p = (p * p) % m

print(ans)
