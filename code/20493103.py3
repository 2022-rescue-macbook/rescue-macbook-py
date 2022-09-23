import sys

queue = []
pri = []
ans = 0


def queue_pop():
    global queue, pri, ans
    can_pop = True

    for i in range(queue[0][1] + 1, 10):
        if pri[i] != 0:
            can_pop = False
            break

    if can_pop:
        pri[queue[0][1]] -= 1
        temp2 = queue[0][0]
        queue.pop(0)
        ans += 1
        return temp2

    else:
        temp2 = queue[0]
        queue.pop(0)
        queue.append(temp2)
        return -1


count = int(sys.stdin.readline().strip())

for i in range(count):
    queue = []
    ans = 0
    pri = [0] * 10 # 1 ~ 9 중요도

    a, b = map(int, sys.stdin.readline().strip().split())

    temp = list(map(int, sys.stdin.readline().strip().split()))

    for index in range(a):
        pri[temp[index]] += 1
        queue.append((index, temp[index]))

    while True:
        if queue_pop() == b:
            print(ans)
            break


