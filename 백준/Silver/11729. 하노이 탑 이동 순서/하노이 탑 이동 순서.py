def hanoi(disks, src, dst, extra):
    if disks == 1:
        hanoi.count += 1
        print(f'{src} {dst}')
    else:
        hanoi(disks - 1, src, extra, dst)
        hanoi.count += 1
        print(f'{src} {dst}')
        hanoi(disks - 1, extra, dst, src)


hanoi.count = 0
n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)