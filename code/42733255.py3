from sys import stdin
input = stdin.readline

for line in range(int(input())):
    N,M = map(int,input().rstrip().split())
    Queue = input().rstrip().split()
    cnt = 0

    while 1:
        
        if max(Queue)!= Queue[0]:
            Queue.append(Queue.pop(0))
            if M==0:
                M=len(Queue)
        else:
            del Queue[0]
            cnt += 1
            if M==0:
                break
        M -= 1
    print(cnt)