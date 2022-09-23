import sys
input = sys.stdin.readline 
for _ in range(int(input())):
    cnt = 0
    N, M = map(int, input().split()) 
    li = list(map(int, input().split()))
    chk = [0] * N; chk[M] = 1 
    while 1:
        if li[0] == max(li):
            cnt += 1 
            if chk[0]: print(cnt); break 
            else: li = li[1:]; chk = chk[1:]
        else:
            li = li[1:] + [li[0]] 
            chk = chk[1:] + [chk[0]]