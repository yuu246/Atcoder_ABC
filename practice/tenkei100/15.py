from itertools import permutations


def distance(list1, list2):
    x1, y1 = list1
    x2, y2 = list2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


N = int(input())
town = []
for i in range(N):
    mati = list(map(int, input().split()))
    town.append(mati)

idx = 0
ans = 0
for arr in permutations([i for i in range(N)]):
    for i in range(N-1):
        x = arr[i]
        y = arr[i+1]
        ans += distance(town[x], town[y])
    idx += 1
ans = ans / idx

print(ans)
