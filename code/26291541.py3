test_case = int(input())

for _ in range(test_case):
    page, where = map(int, input().split())
    priority = list(map(int, input().split()))
    priority_max = int(max(priority))
    count = 0
    check = ["False" for _ in range(len(priority))]
    check[where] = "True"

    while len(priority) != 0:
        if priority[0] < priority_max:
            priority.append(priority.pop(0))
            check.append(check.pop(0))
            
        elif priority[0] == priority_max:
            if check[0] == "True":
                count += 1
                print("{}".format(count))
                break
            else:
                priority.pop(0)
                check.pop(0)
                count += 1
                priority_max = max(priority)
