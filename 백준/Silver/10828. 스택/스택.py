import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.head is None:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def check_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size == 0:
            return -1
        return self.head.data


def judge(oper):
    if oper[0] == 'push':
        Stack.push(oper[1])
    elif oper[0] == 'top':
        print(Stack.top())
    elif oper[0] == 'size':
        print(Stack.check_size())
    elif oper[0] == 'pop':
        print(Stack.pop())
    else:
        print(Stack.empty())


n = int(input())
Stack = stack()
for _ in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    judge(a[:])