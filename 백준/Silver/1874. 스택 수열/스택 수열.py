n = int(input())
card = []
result = []
for _ in range(n):
    card.append(int(input()))
a = 1
b = n
data = []
for i in range(n):
    while a <= card[i]:
        result.append(a)
        data.append('+')
        a += 1
    if card[i] == result[-1]:
        result.pop()
        data.append('-')
    else:
        data.append('NO')
        break

if data[-1] == 'NO':
    print('NO')
else:
    for i in range(len(data)):
        print(data[i])