from sys import stdin, exit

read = lambda : stdin.readline().rstrip()
test = int(read())
# print(test)

for i in range(test):
    read = lambda: stdin.readline().rstrip()
    element = list(map(int,read().split()))
    priority = list(map(int,read().split()))
    # print(element, priority)
    targetidx = element[1]
    count = 0
    while priority:
        # print(priority, targetidx)
        if priority[0] == max(priority):
            if targetidx == 0:
                count += 1
                print(count)
                break
            else:
                count += 1
                priority.remove(priority[0])
                targetidx -= 1
        else:
            if targetidx == 0:
                priority.append(priority[0])
                priority.remove(priority[0])
                targetidx = len(priority) - 1
            else:
                priority.append(priority[0])
                priority.remove(priority[0])
                targetidx -= 1