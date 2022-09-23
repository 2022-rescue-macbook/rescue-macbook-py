import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    Que = list(map(int, input().split()))
    Ind = [i for i in range(N)]
    Print = []
    while True:
        if Que[0] == max(Que):
            Que.pop(0)
            Print.append(Ind.pop(0))
        else:
            Que.append(Que.pop(0))
            Ind.append(Ind.pop(0))
        if len(Print) == N:
            break
    print(Print.index(M)+1)