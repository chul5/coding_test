N = int(input())


def divide(num):
    i = 2
    if num == 1:
        return 1
    while i*i <= num:
        if num % i == 0:
            num = num // i
            print(i)
            return num
        i += 1


def check_prime(num):
    i = 2
    if num == 1:
        return 0
    while i * i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1


while N != 1:
    if check_prime(N) == 0:
        N = divide(N)
    else:
        print(N)
        N = 1