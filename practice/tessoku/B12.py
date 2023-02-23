N = int(input())


def check(x):
    c = x**3 + x
    if c >= N:
        return False
    return True


left = 1
right = 100000

while left < right:
    mid = (left + right) // 2
