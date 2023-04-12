import sys
sys.setrecursionlimit(10**9)

N = int(input())
ans = 0


def f753(x):
    global ans
    x_set = set(str(x))
    if x <= N:
        if '3' in x_set and '5' in x_set and '7' in x_set:
            ans += 1
        f753(10*x+7)
        f753(10*x+5)
        f753(10*x+3)


f753(7)
f753(5)
f753(3)
print(ans)
