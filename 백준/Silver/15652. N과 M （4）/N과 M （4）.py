n, m = map(int, input().split())
card = []
def NM(ans):
    if len(card) == m:
        print(*card)
    else:
        for i in range(ans, n+1):
            card.append(i)
            NM(i)
            card.pop()

NM(1)