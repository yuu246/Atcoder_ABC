from itertools import product

N = int(input())
A_list = list(map(int, input().split()))

Q = int(input())
M_list = list(map(int, input().split()))


def create():
    num_set = set()
    for bit in product((0, 1), repeat=N):
        tmp = 0
        for i in range(N):
            if bit[i] == 1:
                tmp += A_list[i]
        num_set.add(tmp)
    return num_set


can_create_num = create()
for i in range(Q):
    if M_list[i] in can_create_num:
        print('yes')
    else:
        print('no')
