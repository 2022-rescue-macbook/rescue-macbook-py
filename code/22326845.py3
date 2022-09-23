def solution(where,prior):
    cnt = 0
    while True:
        if prior[0] == max(prior):
            cnt += 1#맨앞에 값이 max일때만 프린트 되고 이때만 카운트해야됨
            if where[0] == 1:
                return cnt
            else:
                prior.pop(0)
                where.pop(0)
        else:
            prior.append(prior[0])
            where.append(where[0])
            prior.pop(0)
            where.pop(0)
    
        

T = int(input())
ans = []
for _ in range(T):
    
    N,M = map(int,input().split())#N=100이하의 문서 개수, M=N미만의 목표값의 현재 위치
    prior = list(map(int,input().split()))#1이상9이하의 중요도 N개 주어짐
    where = [0] * N
    where[M] = 1
    ans.append(solution(where,prior))
for i in ans:
    print(i)