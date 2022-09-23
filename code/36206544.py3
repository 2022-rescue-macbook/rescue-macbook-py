from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    queue = []
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))
    cnt = 1
    
    while len(queue) > 1:
        pop = queue.pop(0)
        if pop < max(queue):  # 중요도가 더 높은 게 있다면
            queue.append(pop) # 뒤로 보낸다
            if m == 0:        # 뒤로 보냈는데 만약에 m이 현재 index라면 뒤로 넘김
                m = len(queue)-1
            else:
                m -= 1
        else:                 # 중요도 높은 게 없다면 바로 출력함
            
            if m == 0:        # 만약 그게 m이라면 내보냄
                break         # while문에서 빠져나옴
            m-=1
            cnt+=1
    print(cnt)