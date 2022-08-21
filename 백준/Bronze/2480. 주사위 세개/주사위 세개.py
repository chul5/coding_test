card = list(map(int, input().split()))

def check(n):
    cnt = 0
    for i in range(3):
        if n == card[i]:
            cnt += 1
    return cnt

max_res = 0
temp = []
for i in range(3):
    temp.append(check(card[i]))
    max_res = max(max_res, check(card[i]))

if max_res == 3:
    print(10000+card[i]*1000)
if max_res == 2:
    for i in range(3):
        if temp[i] == max_res:
            print(1000+card[i]*100)
            break
if max_res == 1:
    print(max(card)*100)