a,b,c,d = map(int, input().split())

def str_int(a, b):
    temp = int(str(a) + str(b))
    return temp

print(str_int(a, b) + str_int(c, d))