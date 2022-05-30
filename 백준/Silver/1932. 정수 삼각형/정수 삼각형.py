def max_path(row, col):
    if row == _size - 1:
        return _triangle[row][col]

    if _memo[row][col] == 0:
        _memo[row][col] = _triangle[row][col] + max(max_path(row + 1, col), max_path(row + 1, col + 1))

    return _memo[row][col]


_triangle = []
_size = int(input())
_memo = []
for i in range(_size):
    b = [0 for _ in range(i+1)]
    _memo.append(b)

for _ in range(_size):
    _triangle.append(list(map(int, input().split())))

print(max_path(0, 0))
