import sys
N = int(sys.stdin.readline())
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    q = list(map(int, sys.stdin.readline().split()))
    count = 0
    while not len(q) == 0:
        if max(q) == q[0]:
            if a[1] == 0:
                count += 1
                print(count)
                break
            else:
                q.pop(0)
                a[1] -= 1
                count += 1
        else:
            q.append(q.pop(0))
            a[1] = a[1] - 1 if not a[1] == 0 else len(q) - 1