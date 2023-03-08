#!/usr/bin/env python3


def yakusuu(x):
    yaku = int(x ** 0.5)
    kosuu = 0
    if x == 1:
        return 1
    else:
        for i in range(1, yaku+1):
            if x % i == 0:
                if i * i == x:
                    kosuu += 1
                else:
                    kosuu += 2
        return kosuu


N = int(input())
ans = 0

for i in range(1, N):
    AB = i
    CD = N-i
    AB_yaku = yakusuu(AB)
    CD_yaku = yakusuu(CD)
    ans += (AB_yaku * CD_yaku)

print(ans)
