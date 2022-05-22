def queen(_board, x):
    y = 0
    if x == N:
        queen.count += 1
    else:
        for y in range(N):
            if check_board(_board, x, y) == 1:
                _board.append(y)
                queen(_board, x+1)
                _board.pop()


def check_board(_board, x, y):
    num = 0
    while num < x:
        temp = _board[num] - y
        if temp < 0:
            temp = -temp
        if(_board[num] == y) or (temp == x - num):
            return 0
        num += 1
    return 1


N = int(input())
queen.count = 0
board = []
queen(board, 0)
print(queen.count)