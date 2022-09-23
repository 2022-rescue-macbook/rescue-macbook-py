"""
1966, printer queue
"""

n_case = int(input())

for i in range(n_case):
    n_queue, target = map(int, input().split())
    q = input().split()
    cnt = 0

    while True:
        m = max(q)
        if q[0] == m:
            q.pop(0)
            cnt = cnt + 1
            if target == 0:
                break
            else:
                target = target - 1
        else:
            q.append(q.pop(0))
            if target == 0:
                target = len(q) - 1
            else:
                target = target - 1

    print(cnt)