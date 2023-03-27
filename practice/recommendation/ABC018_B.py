S = input()
N = int(input())


def reverse(S, left, r):
    S = S[:left] + ''.join(reversed(S[left:r])) + S[r:]
    return S


for i in range(N):
    left, r = map(int, input().split())
    left -= 1
    S = reverse(S, left, r)

print(S)
