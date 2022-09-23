import sys
input = sys.stdin.readline
import heapq

t = int(input())

for case in range(t):
    

    heap = []
    n, num = map(int, input().split())
    l = list(map(int, input().split()))
    new = []
    for i in range(0, n):
        heapq.heappush(heap, [-1 * l[i], i])    #최대 힙으로 만들기 위해 -1을 곱함
        new.append([l[i], i])

    mp, mi = heapq.heappop(heap) #가장 큰 우선순위와 해당 인덱스

    np, ni = new.pop(0)           #현재 문서 우선순위와 번호
    cnt = 1

    while l:
        if np == -1 * mp:
            if ni == num:
                print(cnt)
                break
            else:
                mp, mi = heapq.heappop(heap)
                cnt += 1
        
        else:
            new.append([np, ni])

        np, ni = new.pop(0)
        
    
