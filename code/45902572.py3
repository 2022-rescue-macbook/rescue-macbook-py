from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n, m = map(int, stdin.readline().split())

    idx = [0]*n
    idx[m]=-1

    printer = list(map(int, stdin.readline().split()))

    cnt=0
    while 1:    
        now_max = max(printer)
        if(printer[0]==now_max): #최대값이면 -> 뽑아야 함
            cnt+=1
            
            if(idx[0]==-1): #목표값이면 print하고 끝내면 됨
                print(cnt)
                break
            else: #최대값이지만 목표값은 아닌 경우
                printer.pop(0)
                idx.pop(0)

        else:
            printer.append(printer.pop(0))
            idx.append(idx.pop(0))
