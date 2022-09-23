import sys

T=int(sys.stdin.readline())

for i in range(T):
    lst=[]
    TF=1
    num=0
    N, M=map(int, sys.stdin.readline().split())
    lst=list(map(int, sys.stdin.readline().split()))

    while 1:
        lst_sorted=sorted(lst)
        #print('<<<<< lst_sorted', lst_sorted, '>>>>>')
        max_=lst_sorted[-1]
        #print('--------- max', max_, 'lst', lst, '---------')
        while 1:
            if lst[0]!=max_:
                temp=lst[0]
                del lst[0]
                lst.append(temp)
                M-=1
                if M==-1:
                    M+=len(lst)
            elif lst[0]==max_:
                #print('=[del]=', lst[0])
                del lst[0]
                num+=1
                if M==0:
                    TF=0
                break
            #print('--#####-- lst', lst, 'M', M, 'num', num, '--#####--')

        if TF==0:
            break
        M-=1
    
    print(num)
    #print('<--------------------', i, 'end --------------------------->')