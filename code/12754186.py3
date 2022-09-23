def print_q(m, q):
    index = m
    max_num = max(q)
    cnt = 0
    while True:
        temp = q.pop(0)
        if temp < max_num:
            if index == 0:
                q.append(temp)
                index = len(q)-1
            else:
                q.append(temp)
                index -= 1
        else:
            if index == 0:
                cnt += 1
                break
            index -= 1
            cnt += 1
            max_num = max(q)
    return cnt


for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    print(print_q(m, q))    