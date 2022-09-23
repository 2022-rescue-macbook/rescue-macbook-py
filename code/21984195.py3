import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,index = map(int, input().split(" "))
    que = list(map(int,input().split(" ")))
    for i in enumerate(que) :
        if i[0]==index:
            index=i
        que[i[0]] = i
        
    i=0
    while que:
        big = max(que, key = lambda x : x[1])
        i+=1
        if big == index:
            print(i)
            break
        a = que.index(big)
        que = que[a+1:] + que[:a]
