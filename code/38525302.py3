##그냥 큐써서 하는게 빠르겠다 마지막으로 만나는게 쟤가 아닐수도 있나
T = int(input())
for _ in range(T):
    N,M = map(int,input().split()) #개수, 타겟
    q = [int(i) for i in input().split()]
    importance = q[M]
    biggerimportance = q[M]+1
    cnt = 1
    s = set(q)
    pos = N
    
    if max(s) > importance:

        while max(s) > importance:
            biggest = max(s)
            cnt += q.count(biggest)
            for i in range(1,pos+1):
                if q[:pos][-i] == biggest:
                    pos = pos - i
                    s.remove(biggest)
                    break
            else: #index 0까지 왔는데 biggest가 없음 >> 맨끝에서부터 다시 찾아야함
                for i in range(1,N+1): # biggest가 존재는 하니까 그냥 범위 저렇게 잡음
                    if q[-i] == biggest:
                        pos = N - i
                        s.remove(biggest)
                        break
    else: pos = 0 # max(s) == importance 라면 그냥 처음부터 찾으면 됨
    
    if pos <= M:
        for i in range(pos,M):
            if q[i] == importance: cnt += 1
    else:
        for i in q[pos:]:
            if i == importance: cnt += 1
        for i in q[:M]:
            if i == importance: cnt += 1
    print(cnt)