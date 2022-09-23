import sys

num=int(sys.stdin.readline())

for i in range(num):
    NM=list(map(int,sys.stdin.readline().split()))
    Doc=list(map(int,sys.stdin.readline().split()))
    init=0
    result=0

    while Doc:
        if Doc[init]<max(Doc):
            Doc.append(Doc[init])
            Doc.pop(init)
            if NM[1]==init:
                NM[1]=len(Doc)-1
            else:
                NM[1]=NM[1]-1

        else:
            Doc.pop(init)
            result+=1
            if NM[1]==init:
                print(result)
                break
            NM[1] = NM[1] - 1