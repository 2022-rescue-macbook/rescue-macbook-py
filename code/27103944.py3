import sys

T = int(sys.stdin.readline())

answer = []

for i in range(T):
    N,M = map(int,sys.stdin.readline().split())

    prior = list(map(int, sys.stdin.readline().split()))

    idx = list(range(N))    

    idx[M] = "target"

    cnt = 0

    while len(prior) > 0 :
        if prior[0] == max(prior):
            cnt+=1

            if idx[0] == "target":
                answer.append(cnt)
                break
            else:
                del idx[0]
                del prior[0]
        else:
            prior.append(prior[0])
            del prior[0]
            idx.append(idx[0])
            del idx[0]

for i in answer:
    print (i)