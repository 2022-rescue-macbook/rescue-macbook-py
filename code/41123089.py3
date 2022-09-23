import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, i = map(int,sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    temp = [0 for _ in range(n)] # 리스트 안에서 for문 사용 가능
    temp[i] = 1
    cnt = 0
    while True:
        if(queue[0] == max(queue)):
            cnt += 1
            if(temp[0] == 1):
                    print(cnt)
                    break
            else:
                temp.pop(0)
                queue.pop(0)
        else:
            temp.append(temp.pop(0))
            queue.append(queue.pop(0))