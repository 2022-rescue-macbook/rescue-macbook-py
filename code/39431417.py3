import sys

T = int(sys.stdin.readline())
for t in range(T):
    N,M = map(int, sys.stdin.readline().split())
    DOCS = list(map(int, sys.stdin.readline().split()))

    DOCS = [[i,v] for i,v in enumerate(DOCS)]
    prior = max(DOCS, key=lambda x: x[1])[1]

    cnt = 0
    while DOCS:
        x = DOCS.pop(0)
        if x[1] == prior:
            if x[0] == M:
                break
            prior = max(DOCS, key=lambda x: x[1])[1]
            cnt += 1
            continue
        else:
            DOCS.append(x)
    print(cnt+1)