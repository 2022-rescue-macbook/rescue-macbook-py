import sys
input = sys.stdin.readline
num=int(input())
for i in range(num):
    t_num,target=map(int,input().split())
    printer=list(map(int,input().split()))
    index=list(range(t_num))
    count=0
    while True:
        if printer[0]==max(printer):
            count+=1
            if index[0]==target:
                print(count)
                break
            else:
                printer.pop(0)
                index.pop(0)
        else:
            a=printer.pop(0)
            b=index.pop(0)
            printer.append(a)
            index.append(b)