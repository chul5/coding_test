def sum_card(temp):
    sum = 0
    for i in range(len(temp)):
        sum += temp[i]
    return sum



card = []
card2 = []
max_result = 0
for i in range(5):
    card.append(list(map(int, input().split())))

    card2.append(sum_card(card[i]))
    if max_result < card2[i]:
        max_result = card2[i]

for i in range(5):
    if max_result == card2[i]:
        print(i + 1, max_result)