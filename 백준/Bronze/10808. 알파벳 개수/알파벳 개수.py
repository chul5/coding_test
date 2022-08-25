alpha = input()
card = [0] * 26

for i in alpha:
    card[ord(i) - 97] += 1

print(*card)
