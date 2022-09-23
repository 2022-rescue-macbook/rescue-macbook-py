import sys
input=sys.stdin.readline

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    pcnt = [0] * 10
    q = []
    for i, p in enumerate(map(int, input().split())):
        pcnt[p] += 1
        q.append((i, p))
    
    front = 0
    rear = n
    q.append(None)
    cnt = 0
    
    while True:
        idx, p = q[front]
        front = (front + 1) % (n + 1)
        if any(x != 0 for x in pcnt[p + 1:]):
            q[rear] = (idx, p)
            rear = (rear + 1) % (n + 1)
        else:
            pcnt[p] -= 1
            cnt += 1
            if idx == m:
                print(cnt)
                break
