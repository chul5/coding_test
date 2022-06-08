import sys


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class SLL:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def insert(self, data, prev):
#         node = Node(data)
#         self.size += 1
#
#         if prev is None:
#             self.head = node
#         else:
#             node.next = prev.next
#             prev.next = node
#             node.prev = prev
#
#     def remove(self, prev):
#         if self.size == 0:
#             return -1
#         data = prev.next.data
#         prev.next = prev.next.next

card = list(sys.stdin.readline().rstrip())
temp = []
n = int(input())
index = len(card)
for i in range(n):
    check = sys.stdin.readline().split()
    # print(check)
    if check[0] == 'L' and card:
        temp.append(card.pop())
    if check[0] == 'D' and temp:
        card.append(temp.pop())
    if check[0] == 'B' and card:
        card.pop()
    if check[0] == 'P':
        card.append(check[1])

print("".join(card + list(reversed(temp))))