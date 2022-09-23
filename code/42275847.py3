t = int(input())
for _ in range(t):
    each, doc = map(int, input().split())
    important = list(map(int, input().split()))
    q = [0 for _ in range(each)]
    q[doc] = 1
    cnt = 0
    while True:
        if important[0] == max(important):
            cnt += 1
            if q[0] == 1:
                print(cnt)
                break
            else:
                del important[0]
                del q[0]
        else:
            important.append(important[0])
            del important[0]
            q.append(q[0])
            del q[0]