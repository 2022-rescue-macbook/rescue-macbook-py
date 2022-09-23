for _ in range(int(input())) :
    N,M = map(int,input().split())
    priors = list(map(int,input().split()))
    Max_prior,Target_prior = max(priors),priors[M]
    n,p,find = 0,Max_prior,0
    while not find :
        for idx,val in enumerate(priors) :
            if val==p :
                if idx==M :
                    find = n+1
                    break
                else :
                    n,priors[idx] = n+1,0
                    while not p in priors :
                        p-=1
    print(find)