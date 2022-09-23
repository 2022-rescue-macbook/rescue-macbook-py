n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    memo = [0 for _ in range(0,9+1)]
    for i in docs:
        memo[i] +=1

    idocs = []
    for key, val in enumerate(docs):
        idocs.append((val, 1 if key==m else 0))

    cnt=0
    for i in range(9,0,-1):
        while memo[i]:
            tmp = idocs.pop(0)
            if tmp[0] == i:
                memo[i]-=1
                cnt+=1
                if tmp[1]:
                    print(cnt)
            else:
                idocs.append(tmp)

