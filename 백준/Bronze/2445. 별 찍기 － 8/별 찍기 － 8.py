n = int(input())

for i in range(1, n+1):
    print('*' * (i), end='')
    print(' ' * (2*n-2*i), end='')
    print('*' * i)
for i in range(n-1, 0, -1):
    print('*' * i, end ='')
    print(' ' *(2*n-2*i), end ='')
    print('*' * i)