import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n, m = map(int,input().rstrip().split())
    q = list(map(int,input().rstrip().split()))
    priority = [0,0,0,0,0,0,0,0,0]
    for l in q:
        priority[-l] += 1
    count = 0
    index = 0
    while True:
        while priority[index] == 0:
            index += 1
        out = q.pop(0)
        if out == 9 - index:
            count += 1
            if m == 0:
                break
            priority[index] -= 1
        else:
            q.append(out)
        m -= 1
        if m < 0:
            m += len(q)
    print(count)
