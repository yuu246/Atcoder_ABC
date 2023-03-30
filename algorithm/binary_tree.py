class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySerchTree:
    def __init__(self, number_list):
        self.root = None
        for node in number_list:
            self.insert(node)

    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        while True:
            entry = n.data
            if data < entry:
                if n.left is None:
                    n.left = Node(data)
                    return
                n = n.left
            elif data > entry:
                if n.right is None:
                    n.right = Node(data)
                    return
                n = n.right
            else:
                n.data = data
            return

        # 検索機能(インターフェース)
    def search(self, search):
        searcher = self._search_bool(search)
        if searcher is None:
            print("Search target is not found.")
        elif searcher == True:
            print(str(search) + " is found!")
        elif searcher == False:
            print(str(search) + " is not found.")

    # 検索機能本体(出力:boolean),深さ優先探索
    # nodeのvisitedはpopで代用
    def _search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.data == search:
                    return True
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return False

    def inorder(self, node):  # 中順探索 l->r->p^n
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
