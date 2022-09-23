import sys
test_case = int(input())
for _ in range(test_case):
    queue = []
    answer = 0
    docNum, target = map(int, input().split())
    inputdoc = list(map(int, input().split()))
    for i in range(docNum):
        queue.append([i, inputdoc[i]])

    while(True):
        front = queue.pop(0)
        maxpri = max(inputdoc)
        if front[1] == maxpri:
            answer += 1
            if front[0] == target:
                print(answer)
                break
            inputdoc.remove(maxpri)
        else:
            queue.append(front)
