import sys

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    m, cnt = M, 0
    q = list(ARR)
    while True:
        if q[0] < max(q):
            q.append(q.pop(0))
            if 0 == m:
                m = len(q) - 1
            else:
                m -= 1
        else:
            q.pop(0)
            cnt += 1
            if 0 == m:
                break
            else:
                m -= 1
    print(cnt)
