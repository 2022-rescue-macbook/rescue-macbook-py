t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    pps = list(map(int, input().split()))
    chk = [0 for _ in range(n)]
    chk[m] = 'goal'

    cnt = 0
    while pps:
        if pps[0] == max(pps):
            cnt += 1
            if chk[0] == 'goal':
                print(cnt)
                break
            chk.pop(0)
            pps.pop(0)
        else:
            pps.append(pps.pop(0))
            chk.append(chk.pop(0))