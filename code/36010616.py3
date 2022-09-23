import sys
T = int(input())
arr = []
for i in range(T):
    line = sys.stdin.readline().split()
    N = int(line[0])
    targetindex = int(line[1])
    arr = sys.stdin.readline().split()
    for _ in range(len(arr)):
        arr[_] = int(arr[_])
    
    ans = 0
    prio = sorted(arr,reverse=True)
    while 1:
        #print('arr:',arr,'   ','prio','   ',prio,targetindex)
        if arr[0] == prio[0]:
            ans+=1
            if(targetindex == 0):
                print(ans)
                break
            else:
                del arr[0]
                del prio[0]
                targetindex -= 1
        else:
            targetindex -= 1
            if targetindex== -1:
                targetindex = len(arr) - 1
            arr.append(arr[0])
            del arr[0]