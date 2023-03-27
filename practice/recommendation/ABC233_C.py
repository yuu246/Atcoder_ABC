from itertools import product
import math
N, X = map(int, input().split())

hukuro = [list(map(int, input().split()))[1:] for i in range(N)]


ans = 0
for com in product(*hukuro):
    if math.prod(com) == X:
        ans += 1

print(ans)
