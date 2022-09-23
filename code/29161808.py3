import sys
In = sys.stdin.readline
for _ in range(int(In())):
    N, M = map(int, In().split())
    lst = list(map(int, In().split()))

    idx = 0
    while idx < N:
        if idx == M + 1:
            break
        if lst[idx] < max(lst[idx:]):
            lst.append(lst.pop(idx))
            if idx == M:
                M = len(lst) - 1
            else:
                M -= 1
        else:
            idx += 1
    print(M + 1)