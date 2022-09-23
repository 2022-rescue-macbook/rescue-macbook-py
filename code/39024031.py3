import sys

for _ in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    checkList = [0 for _ in range(n)]
    checkList[m] = 1 # 궁금한 문서위치 저장

    cnt = 0
    while True:
        if arr[0] == max(arr):
            cnt+=1

            if checkList[0] != 1:
                del arr[0]
                del checkList[0]
            else:
                print(cnt)
                break
        else:
            arr.append(arr[0])
            checkList.append(checkList[0])
            del arr[0]
            del checkList[0]