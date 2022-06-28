import sys
n = int(input())
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))
card.sort()
for i in range(n):
    print(card[i])