test_case = int(input())
for i in range(test_case):
    length, target_index = list(map(int, input().split(' ')))
    priority = list(map(int, input().split(' ')))

    target = priority[target_index]

    count = 0
    while len(priority) != 0:
        max_num = max(priority)
        if priority[0] == max_num:
            count += 1
            if target_index == 0:
                print(count)
                break
            else:
                priority.pop(0)
                target_index -= 1
        else:
            priority.append(priority.pop(0))
            target_index -= 1
            if target_index < 0:
                target_index = len(priority)-1