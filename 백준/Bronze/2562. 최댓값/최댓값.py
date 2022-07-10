card = []
for _ in range(9):
    card.append(int(input()))
temp = 0
idx = 0
for i in range(9):
    if (temp < card[i]):
        temp = max(temp, card[i])
        idx = i
print(temp)
print(idx+1)