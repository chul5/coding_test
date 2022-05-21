n = int(input())
card = list(map(int, input().split()))


def find_prime(_card):
    i = 2
    if _card <= 1:
        return 0
    while i*i <= _card:
        if _card % i == 0:
            return 0
        i += 1
    find_prime.count += 1
    return 0


find_prime.count = 0
for i in range(n):
    find_prime(card[i])
print(find_prime.count)