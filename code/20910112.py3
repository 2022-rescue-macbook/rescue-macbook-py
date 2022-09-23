a = int(input())
for i in range(a):
    n, target = map(int, input().split())
    Q = (list(map(int, input().split())))
    count = 0
    while True:
        if max(Q) > Q[0]:
            p = Q.pop(0)
            Q.append(p)
            target = (target - 1) % len(Q)
        else:
            count += 1
            if target == 0:
                break
            Q.pop(0)
            target -= 1
    print(count)