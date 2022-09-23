import sys

def solve(n : int,m : int, arr : list):
    if n == 1:
        return 1
    mn = max(arr, key= lambda x :x[1])[1]
    cnt = 0
    m = arr[m]
    while m in arr:

        if arr[0][1] != mn:
            arr.append(arr[0])
            del arr[0]
            
        else :
            del arr[0]
            cnt +=1

            if len(arr)==1 and arr[0] == m:
                return cnt+1
            if len(arr)==1 and arr[0] != m:
                return cnt
            mn = max(arr, key= lambda x :x[1])[1]

    return cnt
            

a = int(sys.stdin.readline())
for i in range(0,a,1):
    n,m = map(int,sys.stdin.readline().split())
    arr = [0]*n
    arr = list(map(int,sys.stdin.readline().split()))
    for j in range(0,len(arr),1):
        arr[j] = [j,arr[j]]
    print(solve(n,m,arr))

