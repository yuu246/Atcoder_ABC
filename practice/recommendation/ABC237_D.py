from collections import deque
N = int(input())
S = input()

left = deque()
right = deque()

for i in range(N):
    if S[i] == 'R':
        left.append(i)
    else:
        right.appendleft(i)

n = deque([N])
ans = left + n + right
print(*ans)
