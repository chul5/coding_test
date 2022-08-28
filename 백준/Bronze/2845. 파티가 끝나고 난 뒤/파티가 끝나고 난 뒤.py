a, b = map(int,input().split())
data = a*b
card = list(map(int,input().split()))
for i in range(5):
    card[i] -= data
print(*card)