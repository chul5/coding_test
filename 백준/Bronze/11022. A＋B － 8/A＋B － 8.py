tc = int(input())

for i in range(1, tc+1):
    a, b = map(int, input().split())
    ans = a + b
    print(f'Case #{i}: {a} + {b} = {ans}')
    