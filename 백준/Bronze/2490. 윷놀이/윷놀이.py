for _ in range(3):
    sum = 0
    card = list(map(int, input().split()))
    for i in range(4):
        if card[i] == 0:
            sum += 1
    if sum == 1:
        print('A')
    if sum == 2:
        print('B')
    if sum == 3:
        print('C')
    if sum == 4:
        print('D')
    if sum == 0:
        print('E')
