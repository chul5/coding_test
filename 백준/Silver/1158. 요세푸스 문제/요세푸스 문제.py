class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prev_node, data):
        node = Node(data)
        self.size += 1

        if prev_node:
            node.next = prev_node.next
            prev_node.next = node
        else:
            self.head = node
            node.next = node

    def traverse(self):
        current = self.head
        while True:
            yield current.data
            if current.next == self.head:
                break
            else:
                current = current.next

    def delete(self, prev_node):
        self.size -= 1
        if prev_node.next != self.head:
            prev_node.next = prev_node.next.next
        else:
            if prev_node != self.head:
                self.head = self.head.next
                prev_node.next = self.head
            else:
                self.head = None


n, k = map(int, input().split())


point = CircularList()
point.insert(None, 1)
# for i in range(n, 1, -1):
#     point.insert(point.head, i)
_current = point.head
for i in range(2, n + 1):
    point.insert(_current, i)
    _current = _current.next

print('<', end='')
#현재위치를 head전을 가리키도록 할 거임!
_current = point.head
for _ in range(n - 1):
    _current = _current.next

while point.size != 1:
    for _ in range(k - 1):
        _current = _current.next
    print(f'{_current.next.data}', end=', ')
    point.delete(_current)
print(f'{point.head.data}', end='>')