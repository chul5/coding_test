def NM_body(card, x):
    if x == M:
        print(*card)
    else:
        for i in range(1, N + 1):
            if check_card(card, x, i) == 1:
                card.append(i)
                NM_body(card, x+1)
                card.pop()


def check_card(card, x, i):
    num = 0
    while num < x:
        if card[num] == i:
            return 0
        num += 1
    return 1


N, M = map(int, input().split())
_card = []
NM_body(_card, 0)