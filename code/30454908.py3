import sys
case=int(sys.stdin.readline().rstrip())

for z in range(case):
    num,pyo=map(int,sys.stdin.readline().rstrip().split())
    sco=list(map(int,sys.stdin.readline().rstrip().split()))
    if num==1:
        print('1')
    elif num==2:
        if pyo==0:
            if sco[1]>sco[0]:
                print('2')
            else:
                print('1')
        else:
            if sco[1]>sco[0]:
                print('1')
            else:
                print('2')
    else:
        qu=[0 for i in range(num*num*2)]
        qu[:num]=sco
        hd=0
        tl=num
        sconum=[0 for i in range(1,10)]
        for i in range(1,10):
            sconum[i-1]=sco.count(i)
        if sco[pyo]==9:
            print(str(sco[:pyo].count(9)+1))
        else:
            target=sco[pyo]
            ans=0
            while(sum(sconum[target:])!=0):
                for i in range(9,target,-1):
                    while sconum[i-1]!=0:
                        if qu[hd]==i:
                            qu[hd]=0
                            hd+=1
                            sconum[i-1]-=1
                            ans+=1
                        else:
                            qu[tl]=qu[hd]
                            qu[hd]=0
                            if hd==pyo:
                                pyo=tl
                            hd+=1
                            tl+=1
            print(str(qu[:pyo].count(target)+1+ans))