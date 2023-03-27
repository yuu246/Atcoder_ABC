class Node:
    def __init__(self, parent=-1, children=None):
        self.parent = parent
        self.children = children


N = int(input())
Tree = {id: Node() for id in range(N)}
for _ in range(N):
    id, *chs = map(int, input().split())
    Tree[id].children = chs
    for ch in chs:
        True[ch].parent = id


def set_depth(id, depth):
    Tree[id].depth = depth
    for ch in Tree[id].children:
        set_depth(ch, depth+1)


for id in Tree:
    if Tree[id].parent == -1:
        set_depth(id, 0)
        break
