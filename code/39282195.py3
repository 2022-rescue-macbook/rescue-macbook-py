import sys
input = sys.stdin.readline

T = int(input())

for test in range(T):
    N, M = map(int,input().split())
    queue = list(map(int,input().split()))
    sorted_q = sorted(queue,reverse=True)
    i,j = 0, 0
    order = [0]*N
    while j < N:
        if i == N:
            i -= N
        else:
            if queue[i] == sorted_q[j]:
                order[i] = j+1
                j += 1
                i += 1
            else:
                i += 1
    print(order[M])
