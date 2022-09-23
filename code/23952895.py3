test_case = int(input())
answer = []
for _ in range(test_case):
    n, m = map(int,input().split())
    queue = list(map(int, input().split()))
    target_queue = list(range(len(queue)))
    target_queue[m] = 'target'
    pop_order = 0
    while(True):
        if(queue[0]==max(queue)):
            pop_order += 1
            if(target_queue[0] == 'target'):
                answer.append(pop_order)
                break
            else:
                queue.pop(0)
                target_queue.pop(0)
        else:
            queue.append(queue.pop(0))
            target_queue.append(target_queue.pop(0))

for i in answer:
    print(i)