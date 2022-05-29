n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
sorted_B = sorted(B)
sum = 0
for i in range(n):
    sum += A[i] * sorted_B[i]
print(sum)