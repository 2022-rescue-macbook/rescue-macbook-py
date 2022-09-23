import sys
input = sys.stdin.readline
n = int(input().rstrip())


for _ in range(n):
    m,k = map(int,input().rstrip().split())
    prt = list(map(int,input().rstrip().split()))
    ind = [i for i in range(len(prt))]
    
    
    cnt = 0
    while True:
        max_temp = max(prt)
        
        if prt[0] == max_temp:
            if ind[0] == k:
                cnt += 1
                break
            else:
                prt.pop(0)
                ind.pop(0)
                cnt += 1
        else:
            a = prt.pop(0)
            b = ind.pop(0)
            prt.append(a)
            ind.append(b)
    print(cnt)
    
            
            
            
    
    
                
                
                
        
        
        
                
        
        
        
        

    
    
    
    