from itertools import product, permutations, combinations, combinations_with_replacement
from functools import lru_cache, reduce
from heapq import heapify, heappush, heappop
from collections import deque, defaultdict, Counter
from bisect import bisect_right, bisect_left
import random
import math
import sys
def input(): return sys.stdin.readline().rstrip()


inf = float('inf')


def error(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end, file=sys.stderr)


# mod = 1000000007
# mod = 998244353
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sys.setrecursionlimit(7*10**5)

#  -----------------------  #
