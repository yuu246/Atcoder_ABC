def solver(N, S1, S2, S3):
    S1 = S1 + S1
    S2 = S2 + S2
    S3 = S3 + S3
    S1_set = set()
    S2_set = set()
    S3_set = set()
    for i in range(0, 2*N):
        S1_part = S1[i: i+2*N+1]
        S2_part = S2[i: i+2*N+1]
        S3_part = S3[i: i+2*N+1]
        S1_set.add(S1_part)
        S2_set.add(S2_part)
        S3_set.add(S3_part)
    ans_set = S1_set & S2_set & S3_set
    ans_list = list(ans_set)
    print(ans_list[0])


T = int(input())

for _ in range(T):
    N = int(input())
    S1 = input()
    S2 = input()
    S3 = input()
    solver(N, S1, S2, S3)
