N=int(input())

for _ in range(N):
    num, index = map(int,input().split())
    serious=list(map(int,input().split()))
    cnt = 0
    
    while serious:

        if serious[0] < max(serious):
            serious.append(serious.pop(0))
            
            if index == 0:
                index = len(serious)-1
            else:
                index-=1
        else:
            serious.pop(0)
            cnt+=1
            
            if index==0:
                break
            else:
                index-=1
    print(cnt)
  