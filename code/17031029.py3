test_case = int(input())

for i in range(test_case):
    N, M = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0
    while True:
        if queue[0][0] == max(queue)[0]:
            count +=1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
