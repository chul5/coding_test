import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def check_size(self):
        return self.size

    def check_empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        return self.head.data

    def back(self):
        if self.size == 0:
            return -1
        return self.tail.data

n = int(input())
queue = Queue()
for i in range(n):
    card = sys.stdin.readline().split()
    if card[0] == 'push':
        queue.enqueue(card[1])
    if card[0] == 'pop':
        print(queue.dequeue())
    if card[0] == 'size':
        print(queue.check_size())
    if card[0] == 'empty':
        print(queue.check_empty())
    if card[0] == 'front':
        print(queue.front())
    if card[0] == 'back':
        print(queue.back())