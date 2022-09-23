import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    info = list(map(int, input().strip().split()))
    info = [[x, idx] for idx, x in enumerate(info)]
    ans = 0
    while True:
        if info[0][0] == max(info)[0]:
            ans += 1
            if info[0][1] == m:
                print(ans)
                break
            else:
                info = info[1:]
        else:
            info = info[1:] + info[:1]

