import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    list_length, target_idx = map(int, sys.stdin.readline().split())
    priority_list = list(map(int, sys.stdin.readline().split())) # [1, 2, 3, 4]
    count = 1

    while True:
        if max(priority_list) != priority_list[0]:
            if target_idx == 0:
                target_idx = len(priority_list)
            priority_list.append(priority_list.pop(0))
            target_idx -= 1
        else:
            if target_idx == 0:
                print(count)
                break
            else:
                priority_list.pop(0)
                count += 1
                target_idx -= 1