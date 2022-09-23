import sys
K=int(sys.stdin.readline())
for i in range(K):
    N,M=map(int,sys.stdin.readline().split())
    Plist=list(map(int,sys.stdin.readline().split())) #Priority list
    # print(Plist)
    Rlist=[i for i in range(N)] #실제 원소 리스트
    FindE=Rlist[M] #FindE 찾고자 하는 원소
    # print(Rlist)
    Ptlist=[]  #출력 순서 담기는 리스트

    # while not Plist==[]:
    #     o=max(Plist)
    #     while not Plist[0]==o:
    #         Plist.append(Plist[0])
    #         Plist.pop(0)
    #     Ptlist.append(Plist[0])
    #     Plist.pop(0)
    # print(Ptlist)
    # print(Plist)

    while not Plist==[]:
        o=max(Plist)
        while not Plist[0]==o:
            Plist.append(Plist[0])
            Plist.pop(0)
            Rlist.append(Rlist[0])
            Rlist.pop(0)
        Ptlist.append(Rlist[0])
        Plist.pop(0)
        Rlist.pop(0)
    
    print(Ptlist.index(FindE)+1)