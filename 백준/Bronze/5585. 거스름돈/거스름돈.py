n = 1000 - int(input())
count = 0
card = [500, 100, 50, 10, 5, 1]

for i in card:
    k = n // i
    count += k
    n %= i

print(count)