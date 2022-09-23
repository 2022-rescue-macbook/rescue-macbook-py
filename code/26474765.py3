cases=int(input())
answer=[]
for i in range(cases):
    fst=input().split()
    leng = int(fst[0])
    target= int(fst[1])
    arr=list(map(int,input().split()))
    count = 0
    curs=0
    while True:
        if arr[curs]==max(arr):
            count+=1
            if curs==target:
                answer.append(count)
                break
        else:
            arr.append(arr[curs])
            if curs==target:
                target=(len(arr)-1)
        arr.pop(0)
        target -=1
for k in answer:
    print(k)  