n, m = map(int, input().split())

def bit_str(card):
    if len(card) == m:
        print(*card)
    else:
        for i in range(1, n + 1):
            card.append(i)
            bit_str(card)
            card.pop()

bit_str([])