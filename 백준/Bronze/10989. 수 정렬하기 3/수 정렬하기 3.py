import sys
n = int(input())

card = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    card[num] += 1

for i in range(10001):
    if card[i] != 0:
        for j in range(card[i]):
            print(i)