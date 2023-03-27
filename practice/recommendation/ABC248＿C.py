from collections import defaultdict
from bisect import bisect_right, bisect_left
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

idx_dict = defaultdict(list)
for i in range(0, N):
    idx_dict[A[i]].append(i)
key = idx_dict.keys()

for k in list(key):
    idx = idx_dict[k]
    idx.sort()

for i in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    idx_list = idx_dict[X]
    left = bisect_left(idx_list, L)
    right = bisect_right(idx_list, R)
    print(right-left)
