T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    paper = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
    cnt = 0
    while paper:
        p = paper.pop(0)
        if any(p[1] < x[1] for x in paper):
            paper.append(p)
        else:
            cnt += 1
            if p[0] == M:
                print(cnt)
                break