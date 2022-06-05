size = int(input())
card =[]
for _ in range(size):
    card.append(list(map(int, input().split())))

memo = []
for i in range(1, size + 1):
    memo.append([None] * i)


def tri(row, col):
    if row == size - 1:
        return card[row][col]
    max_result = 0
    if memo[row][col] is None:
        max_result = card[row][col] + max(tri(row+1,col), tri(row+1,col+1))
        memo[row][col] = max_result
    return memo[row][col]


print(tri(0,0))