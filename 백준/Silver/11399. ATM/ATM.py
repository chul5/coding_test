
n = int(input())
card = list(map(int, input().split()))
sum = 0
result = 0
card.sort()
for i in range(n):
    sum += card[i]
    result +=sum
print(result)