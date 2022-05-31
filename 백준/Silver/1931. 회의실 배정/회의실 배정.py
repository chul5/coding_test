import sys


def selector(act):
    selected_act = 0
    ans = [selected_act]

    for i in range(1, len(act)):
        if act[i][0] >= act[selected_act][1]:
            selected_act = i
            ans.append(selected_act)
    return ans


n = int(input())
acts = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    acts.append((a, b))

acts.sort(key=lambda x: (x[1], x[0]))
print(len(selector(acts)))

