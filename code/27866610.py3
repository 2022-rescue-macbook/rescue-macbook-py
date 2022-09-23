T = int(input())

ans = []
for _ in range(T):
    N, M = map(int,input().split())
    prior = list(map(int,input().split())) #length == N
    prior = list(enumerate(prior))
    cnt=1
    while True:
        max_val = max(prior,key=lambda x:x[1])
        index = prior.index(max_val)
        prior = prior[index:] + prior[:index]
        print_val = prior.pop(0)
    
        if print_val[0] == M:
            ans.append(cnt)
            break
        cnt+=1

print(*ans,sep='\n')

