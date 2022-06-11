from collections import deque
import sys

deq = deque([])
n = int(input())

for i in range(n):
    card = sys.stdin.readline().split()
    if card[0] == 'push_back':
        deq.append(card[1])
    if card[0] == 'push_front':
        deq.appendleft(card[1])
    if card[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if card[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    if card[0] == 'pop_front':
        if (len(deq)) == 0:
            print(-1)
        else:
            print(deq.popleft())
    if card[0] == 'pop_back':
        if (len(deq)) == 0:
            print(-1)
        else:
            print(deq.pop())
    if card[0] == 'size':
        print(len(deq))
    if card[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)