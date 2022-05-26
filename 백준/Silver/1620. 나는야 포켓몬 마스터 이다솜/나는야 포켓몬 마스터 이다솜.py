import sys

class Node:
    def __init__(self, data=None, num=None):
        self.data = data
        self.num = num
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, num):
        node = Node(data, num)
        parent = None
        current = self.root

        while current:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right
        if parent is None:
            self.root = node
        elif node.data <=parent.data:
            parent.left = node
        else:
            parent.right = node

    def search(self, data):
        node = self.root
        while True:
            if node is None:
                return node
            elif node.data == data:
                return node.num
            elif data < node.data:
                node = node.left
            else:
                node = node.right


n, m = map(int, input().split())
name_list = []
tree = Tree()
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip('\n')
    name_list.append(name)
    # name = name.lower()
    tree.insert(name, i)

for j in range(m):
    name = sys.stdin.readline().rstrip('\n')
    if name.isdigit():
        print(name_list[int(name) - 1])
    else:
        a = tree.search(name)
        print(a)