def check_prime(num):
    i = 2
    if num == 1:
        return 0
    while i * i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1


card = []
sum = 0
M = int(input())
N = int(input())
for i in range(M, N+1):
    if check_prime(i) == 1:
        card.append(i)
if len(card) != 0:
    for i in range(len(card)):
        sum += card[i]
    print(sum)
    print(card[0])
else:
    print(-1)