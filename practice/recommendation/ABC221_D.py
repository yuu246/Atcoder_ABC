from collections import defaultdict
N = int(input())
player = []
for i in range(N):
    a, b = map(int, input().split())
    player.append([a, a+b])
mapping = defaultdict(int)
player.sort()

for p in player:
    s, g = p
    mapping[s] += 1
    mapping[g] -= 1

key = list(mapping.keys())
key.sort()
count = 0
ans = [0] * (N+1)
for i in range(len(key)):
    count += mapping[key[i]]
    if i != len(key)-1:
        num = key[i+1] - key[i]
        ans[count] += num
print(*ans[1:])
