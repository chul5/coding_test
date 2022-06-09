def find_GCD(x, y):
    while y:
        x, y = y,(x%y)
    return x

def find_LCM(x, y):
    result = (x*y)//find_GCD(x,y)
    return result

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(find_LCM(a, b))