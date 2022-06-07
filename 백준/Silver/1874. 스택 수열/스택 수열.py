n = int(input())
result = []
a = 1
data = []
for i in range(n):
    card = int(input())
    while a <= card:
        result.append(a)
        data.append('+')
        a += 1
    if card == result[-1]:
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