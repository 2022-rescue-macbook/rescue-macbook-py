import sys

#함수
def functions(m, queue, cnt):
    while(1):
        notice = 1
        for i in range(1, len(queue)):
            if(queue[0][1] < queue[i][1]):
                queue.append(queue[0])
                del queue[0]
                notice = 0
                break
        if(notice == 0):
            continue
        else:
            cnt += 1
            if(queue[0][0] == m):
                break
            else:
                del queue[0]
    return cnt


#입력 갯수
ip = int(input())

list1 = []
list2 = []
for i in range(ip):
    list1.clear()
    list2.clear()
    N, M = map(int, input().split())
    list1 = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        list2.append([j, list1[j]])
    print(functions(M, list2, 0))
    
                
    