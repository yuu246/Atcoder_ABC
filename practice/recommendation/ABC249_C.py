from collections import defaultdict
N, K = map(int, input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)
ALL = 2**N
ans_set = set()
ans = -10
for bit in range(ALL):
    tmp = 0
    count = defaultdict(int)
    for i in range(N):
        if bit & 1 << i > 0:
            for x in S[i]:
                count[x] += 1
    key = count.keys()
    for i in key:
        if count[i] == K:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
