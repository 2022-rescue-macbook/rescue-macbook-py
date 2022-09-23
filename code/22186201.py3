n = int(input())
for i in range(n):
    p, q = map(int, input().split())
    stack = []
    priority = list(map(int, input().split()))
    for j in range(p):
        stack.append((j, priority[j]))
    c = 1
    while True:
        now = stack.pop(0)
        pr = now[1]
        for j in stack:
            if pr < j[1]:
                stack.append(now)
                now = (-1, -1)
                break
        if now[0] == q:
            print(c)
            break
        elif now[0] != -1:
            c += 1