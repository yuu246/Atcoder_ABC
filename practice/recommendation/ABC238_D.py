
T = int(input())

for i in range(T):
    a, s = map(int, input().split())
    if (s - 2*a) & a == 0 and 2*a <= s:
        print('Yes')
    else:
        print('No')
