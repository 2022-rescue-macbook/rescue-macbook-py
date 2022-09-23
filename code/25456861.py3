num = int(input())

for i in range(num):
    N,M = map(int,input().split())
    arr= list(map(int,input().split()))
    brr= [0 for _ in range(N)]
    brr[M] = 1
    rank = 1
    
    while(len(arr)):
        if arr[0] == max(arr):
            if brr[0] == 1:
                break;
            else:
                arr.pop(0)
                brr.pop(0)
                rank +=1
        else:
            arr.append(arr.pop(0))
            brr.append(brr.pop(0))
                
    print(rank)