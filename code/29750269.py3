import sys
nm=[]
arr=[]
result = []
n = int(input())

for _ in range(n):
    nm.append(list(map(int,sys.stdin.readline().rstrip().split()))) 
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

index = 0
for i in range(n):
    index = nm[i][1]
    lenth = nm[i][0] 
    cnt=0 
    while True:
        for j in range(lenth):
            if arr[i][j] == max(arr[i]) : 
                arr[i][j] = 0
                cnt+=1
            if arr[i][j] == 0 and j ==index :
                result.append(cnt)
                break  
        if arr[i][index] == 0: break 

print(str(result).replace('[','').replace(']','').replace(',','\n').replace(' ',''))