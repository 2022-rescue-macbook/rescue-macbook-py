test_case=int(input())

for _ in range(test_case):
    t,answer=list(map(int, input().split(' ')))
    rank=list(map(int, input().split(' ')))

    count=0

    # m=max()
    while True:
        m=max(rank)
        p=rank.pop(0)
        if p==m:
            count+=1
            if answer==0:
                print(count)
                break
            else:
                answer-=1  
            
        else:
            rank.append(p)
            answer-=1
            if answer==-1:
                answer=len(rank)-1
