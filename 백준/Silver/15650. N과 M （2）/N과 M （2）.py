def NM_body(card, x):
    if x == M:
        print(*card)
    else:
        for i in range(1, N + 1):
            card.append(i)
            if check_card(card, x) == 1:
                NM_body(card, x + 1)
            card.pop()


def check_card(card, x):
    num = 0
    while num < x:
        if card[num] == card[x] or card[num] > card[x]:
            return 0
        num += 1
    return 1


N, M = map(int, input().split())
_card = []
NM_body(_card, 0)