n = int(input())
target_list = list(map(int, input().split()))
target_list.sort()


def binary_search(ordered_list, target):
    left, right = 0, len(ordered_list)-1
    while left <= right:
        mid = (left + right) // 2
        if target > ordered_list[mid]:
            left = mid + 1
        elif target < ordered_list[mid]:
            right = mid - 1
        else:
            return 1
    return 0


m = int(input())
finder_list = list(map(int, input().split()))
for i in range(m):
    a = binary_search(target_list, finder_list[i])
    print(a)