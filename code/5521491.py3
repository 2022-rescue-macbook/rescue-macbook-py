testcase = int(input())

for i in range(testcase):
    n, m = map(int, input().split())
    priority = list(input().split())
    p = [int(i) for i in priority]
    cnt = 0

    while True:
        if p[0] == max(p):
            cnt += 1
            p.pop(0)
            m -= 1
            if len(p) == 0:
                break

            else:
                if m == -1:
                    break
        else:
            p.append(p.pop(0))
            if m == 0:
                m = len(p) - 1
            else:
                m -= 1

    print(cnt)
