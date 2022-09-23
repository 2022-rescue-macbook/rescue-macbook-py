test_case = int(input())
result_list = []
for _ in range(test_case):
    num, seq = map(int, input().split())
    queue = list(map(int, input().split()))
    result = 0
    while True:
        if queue[0] == max(queue):
            queue.pop(0)
            result+=1
            if seq == 0:
                result_list.append(result)
                break
        else:
            queue.append(queue.pop(0))
        if seq == 0:
            seq = len(queue)-1
        else:
            seq -= 1
for i in result_list:
    print(i)