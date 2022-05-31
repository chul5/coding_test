import sys

n = int(input())
acts = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    acts.append((a, b))

acts.sort(key=lambda x: (x[1], x[0]))


def selector(s: list):
    selected_act = 0
    ans = [s[selected_act]]

    for act in range(1, len(s)):
        if s[act][0] >= s[selected_act][1]:
            selected_act = act
            ans.append(s[selected_act])

    return len(ans)

print(selector(acts))