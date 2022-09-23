import sys 
input = sys.stdin.readline

test = int(input())

for _ in range(test) : 
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    idx = [0 for _ in range(n)]
    idx[m] = 1 
    
    cnt = 0
    while True:
        if lst[0] == max(lst) :
            cnt += 1 
            
            if idx[0] != 1:
                del lst[0]
                del idx[0]
            else : 
                print(cnt)
                break
        else : 
            lst.append(lst[0])
            idx.append(idx[0])
            del lst[0]
            del idx[0]
            