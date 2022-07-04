import sys

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    # index number is necessary
    def float_up(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = \
                self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float_up(self.size)

    def min_index(self, k):
        left = k * 2
        right = k*2 + 1
        if right > self.size:
            return left
        elif self.heap[left] < self.heap[right]:
            return left
        else:
            return right

    def sink(self, k):
        while k*2 <= self.size:
            mi = self.min_index(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = \
                self.heap[mi], self.heap[k]
            k = mi

    def pop(self):
        if self.size == 0:
            return 0
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return item

    def heap_sort(self):
        sorted_list = []
        for _ in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list

h = MinHeap()

n = int(input())
for i in range(n):
    m = int(sys.stdin.readline())
    m = -m
    if m == 0:
        print(-h.pop())
    else:
        h.insert(m)