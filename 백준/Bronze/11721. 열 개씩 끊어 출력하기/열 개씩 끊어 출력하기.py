n = input()
cnt = 0
for i in n:
    cnt += 1
    print(i, end='')
    if cnt % 10 == 0:
        print('')
