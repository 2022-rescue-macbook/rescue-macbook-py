import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    doc = list(map(int, sys.stdin.readline().split()))
    idx = []
    for i in range(n):
        idx.append(i)
    cnt = 0
    x = 101

    while doc:
        for i in range(1, len(doc)):
            if doc[0] < doc[i]:
                doc.append(doc.pop(0))
                idx.append(idx.pop(0))
                break

        if max(doc) == doc[0]:
            doc.pop(0)
            x = idx.pop(0)
            cnt += 1
        if x == m:
            print(cnt)
            break
