def push(data, a):
    data.append(a)
    
def pop(data):
    tmp = data[0]
    data.remove(data[0])
    return tmp

import sys

t = int(input())
for i in range(t):
    N, M = map(int, sys.stdin.readline().split()) # M은 찾고싶은 값

    queue = [[i,''] for i in map(int, sys.stdin.readline().split())]
    rank = [queue[i][0] for i in range(len(queue))] ; rank.sort() # 이렇게안하면 큐랑 똑같아짐.. 별명개념 ㅠ +[]
    queue[M][1] = 'check'
    count = 0

    while True:

        if rank[-1] == queue[0][0]: # 맨 앞이 젤 큰 수일 경우, 제거, 카운트 +1
            if queue[0][1] == 'check': # 맨 앞이 젤 큰수이며 check 인 경우 멈춘다! ★
                break
            pop(queue)
            del rank[-1]
            count = count +1
        else:                     # 맨 앞이 젤 큰수가 아니면, 뒤로 보낸다.
            push(queue, pop(queue))
        
    print(count+1) 