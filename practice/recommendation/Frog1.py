import sys
sys.setrecursionlimit(10**9)

N = int(input())
H = list(map(int, input().split()))

cost = [-1] * (N+1)
done = [False] * (N+1)


def rec(n):
    if done[n]:
        return cost[n]
    if n == 1:
        cost[n] = 0
    elif n == 2:
        cost[n] = rec(n-1) + abs(H[n-1]-H[n-2])
    else:
        cost[n] = min(rec(n-1) + abs(H[n-1] - H[n-2]),
                      rec(n-2) + abs(H[n-1] - H[n-3]))
    done[n] = True
    return cost[n]


print(rec(N))
