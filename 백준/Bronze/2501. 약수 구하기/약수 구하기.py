a, b = map(int,input().split())
i = 1
card =[]
while(i <= a):
    if a % i == 0:
        card.append(i)
    i += 1

if len(card) < b:
    print(0)
else:
    print(card[b -1])