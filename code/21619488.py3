testcase = int(input())
for i in range(testcase):
    queue = []
    count = 0
    docx_total, target_index = map(int, input().split())
    prior = input().split()
    for i in range(docx_total):
        queue.append(int(prior[i]))
    while True:
        if max(queue) > queue[0]:
            if target_index == 0:
                target_index = len(queue) - 1
                temp = queue[0]
                del queue[0]
                queue.append(temp)
            else:
                target_index -= 1
                temp = queue[0]
                del queue[0]
                queue.append(temp)
        elif max(queue) == queue[0]:
            if target_index == 0:
                print(count + 1)
                break
            else:
                target_index -= 1
                count += 1
                del queue[0]