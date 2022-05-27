import copy


def check_move(graph, row, col, color):
    if row < 0 or row >= size:
        return False
    if col < 0 or col >= size:
        return False
    if graph[row][col] != color:
        return False
    if graph[row][col] == 'X':
        return False
    return True


def breadth_first_search(graph, row, col):
    # if graph[row][col] != 'X':
    #     breadth_first_search.count += 1
    color = graph[row][col]
    graph[row][col] = 'X'
    stack = [(row, col)]
    # move left, right, down, up
    move = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    while len(stack):
        row, col = stack.pop()
        for m in range(4):
            next_row, next_col = row, col
            next_row += move[m][0]
            next_col += move[m][1]

            if not check_move(graph, next_row, next_col, color):
                continue
            stack.append((next_row, next_col))
            graph[next_row][next_col] = 'X'


size = int(input())
RGB_card = []
# breadth_first_search.count = 0
for i in range(size):
    RGB_card.append([])
for i in range(size):
    RGB_card[i] = list(input())

copied_RB = copy.deepcopy(RGB_card)
copied_RGB = copy.deepcopy(RGB_card)
for i in range(size):
    for j in range(size):
        # 적록색약!
        if copied_RB[i][j] == 'G':
            copied_RB[i][j] = 'R'

RB_count = 0
RGB_count = 0
for i in range(size):
    for j in range(size):
        if copied_RB[i][j] != 'X':
            RB_count += 1
            breadth_first_search(copied_RB, i, j)
        if copied_RGB[i][j] != 'X':
            RGB_count += 1
            breadth_first_search(copied_RGB, i, j)

print(RGB_count, RB_count)