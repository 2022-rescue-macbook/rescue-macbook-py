T = int(input())
for testcase in range(T):
    N, M = map(int, input().split())
    waitingList = list(map(int, input().split()))
    cnt = 0;
    while(True):
        if waitingList[0] == max(waitingList):
            cnt += 1
            if not M:
                print(cnt)
                break
            del waitingList[0]
            M -= 1
            
        else:
            waitingList.append(waitingList[0])
            del waitingList[0]
            if M:
                M -= 1
            else:
                M = len(waitingList)-1