import sys
input = sys.stdin.readline



T = int(input())
for _ in range(T):
    A, B =map(int, input().split())
    C= list(map(int, input().split()))
    Q=[]
    if A==1:
        print(1)
    else:
        for i in range(len(C)):
            Q.append([C[i],i])
        C = sorted(C)
        cnt=0
        while True:
            if Q[0][0] == C[-1]:
                cnt += 1
                if Q[0][1] == B:
                    print(cnt)
                    break
                else:
                    Q.pop(0)
                    del C[-1]

            else:
                Q.append(Q.pop(0))
