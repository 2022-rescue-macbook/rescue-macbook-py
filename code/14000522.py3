def wow(find,arr):
    index = find
    delcase = max(arr)
    cnt = 0
    while True:
        if arr[0] == delcase:
            if index==0:
                cnt+=1
                break
            else:
                cnt+=1
                arr.pop(0)
                index -=1
                delcase = max(arr)
        else :
            if index==0:
                arr.append(arr.pop(0))
                index = len(arr)-1
            else :
                index -=1
                arr.append(arr.pop(0))
    return cnt

testcase = int(input())

for _ in range(testcase):
    n,find = map(int,input().split())
    arr = list(map(int,input().split()))
    print(wow(find,arr))