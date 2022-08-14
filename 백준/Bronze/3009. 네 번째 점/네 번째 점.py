def count_x(n):
    cnt = 0
    for i in range(3):
        if card[i][0] == n:
            cnt += 1
    return cnt

def count_y(n):
    cnt = 0
    for i in range(3):
        if card[i][1] == n:
            cnt += 1
    return cnt

card = []
for _ in range(3):
     card.append(list(map(int, input().split())))

a = 0
b = 0

for i in range(3):
    if count_x(card[i][0]) == 1:
        a = card[i][0]
    if count_y(card[i][1]) == 1:
        b = card[i][1]
print(a, b)