for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    ps = list(range(n))
    cnt = 0
    while 1:
        e = queue.pop(0)
        p = ps.pop(0)
        if queue:
            if e >= max(queue):
                cnt += 1
                if p == m:
                    break
            else:
                queue.append(e)
                ps.append(p)
        else:
            cnt += 1
            break
    print(cnt)