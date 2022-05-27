from collections import deque


def breadth_first_search(graph, root):
    visited = []
    discovered = []
    queue = deque([root])
    discovered.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        visited.append(node)
        undiscovered = set(graph[node]).difference(set(discovered))

        if len(undiscovered) > 0:
            for elem in sorted(undiscovered):
                queue.append(elem)
                discovered.append(elem)

    return visited


n = int(input())
m = int(input())
graph = []
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x = breadth_first_search(graph, 1)
print(len(x) - 1)