S = input()

card = []
for i in range(len(S)) :
    card.append(S[i:])

card.sort()
for i in card:
    print(i)