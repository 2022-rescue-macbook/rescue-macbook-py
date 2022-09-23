list2=[]
for i in range(int(input())) :
    N,M = map(int,input().split())
    list1 = list(map(int,input().split()))
    Max_list=max(list1)
    Target_list = list1[M]
    n=0
    find = 0
    while not find :
        for idx,val in enumerate(list1) :
            if val==Max_list :
                if idx==M :
                    find = n+1
                    break
                else :
                    n,list1[idx] = n+1,0
                    while not Max_list in list1 :
                        Max_list-=1
    list2.append(str(find))
print("\n".join(list2))