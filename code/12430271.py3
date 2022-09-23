queue = int(input())
for _ in range(queue):
    NM = list(map(int,input().split(' ')))
    N = NM[0]
    M = NM[1]
    imp = list(map(int,input().split(' ')))
    judge = [0 for _ in range(N)]
    judge[M] = 'queue'
    cnt = 0
    if len(imp) == N:
        while True:
            if imp[0] == max(imp):
                cnt += 1
                if judge[0] == 'queue':
                    print(cnt)
                    break
                else:
                    imp.pop(0)
                    judge.pop(0)
            else:
                imp.append(imp.pop(0))
                judge.append(judge.pop(0))