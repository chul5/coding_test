class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        self.size += 1
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.size == 0:
            return -1
        self.size -= 1
        data = self.top.data
        self.top = self.top.next
        return data

n = int(input())
Stack = stack()
for _ in range(n):
    a = list(input().split())
    for i in a:
        for j in i:
            Stack.push(j)

        for _ in i:
            print(Stack.pop(), end='')
        print(' ', end='')
    print('')