import sys
read = lambda : sys.stdin.readline()
answers = []
for _ in range(int(read())):
    size, index = map(int, read().split(' '))
    que = list(map(int, read().split(' ')))
    count = 0
    while True:
        if(que[0] == max(que)):
            x = que.pop(0)
            count += 1
            if(index == 0):
                break
            else:
                index = int((index - 1) % len(que))
        else:
            que.append(que.pop(0))
            index = int((index - 1) % len(que))
    answers.append(count)
for answer in answers:
    print(answer)