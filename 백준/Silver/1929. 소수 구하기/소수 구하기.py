m, n = map(int, input().split())

def check_prime(num):
    i = 2
    if num <= 1:
        return 0
    while i <= num//i:
        if num % i ==0:
            return 0
        i += 1
    return 1

for i in range(m, n+1):
    if check_prime(i) == 1:
        print(i)