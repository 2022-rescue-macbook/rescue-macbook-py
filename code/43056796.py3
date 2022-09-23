import sys

case = int(sys.stdin.readline())

for i in range(case):
    num_of_docu, turn = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    queue = temp[:]
    temp.sort(reverse=True)

    cnt = 0
    while True:
        if temp[0] != queue[0]:
            front = queue.pop(0)
            queue.append(front)
            if turn == 0:
                turn = len(queue)
            turn -= 1
        else:
            if turn == 0:
                cnt += 1
                break
            else:
                temp.pop(0)
                queue.pop(0)
                cnt += 1
                turn -= 1
    print(cnt)