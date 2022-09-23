import sys
T = int(sys.stdin.readline())

for i in range(T):
    ans = 0
    N, M = map(int, sys.stdin.readline().split())
    tc = list(map(int, sys.stdin.readline().split()))
    tm = [0] * N
    tm[M] = 1
    popData = max(tc)
    while True:
        tempM = tm.pop(0)
        tempC = tc.pop(0)
        if tempC == popData:
            ans += 1
            if tempM == 1:
                break
            popData = max(tc)
        else:
            tc.append(tempC)
            tm.append(tempM)
    print(ans)