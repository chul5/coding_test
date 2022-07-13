
a, b, c, d = map(int, input().split())
x1 = abs(0-a)
x2 = abs(c-a)

y1 = abs(0-b)
y2 = abs(b-d)
print(min(min(x1,x2), min(y1,y2)))