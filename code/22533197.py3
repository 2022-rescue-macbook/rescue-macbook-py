import heapq as hq
n_test = int(input())
for _ in range(n_test):
    N, M = map(int, input().split())
    #N : 문서의 수 
    #M : 궁금한 문서의 현재 위치
    '''
    가장 앞에 있는 문서의 중요도 확인
    나머지 문서들중 현재 문서보다 중요도가 높은 문서가
    하나라도 있다면 Q에 가장 뒤에 배치

    현재 가장 중요한 
    '''
    importance =list(map(int, input().split())) #N개의 문서에 대한 중요도
    priority = sorted(importance, reverse=True)
    importance =[(i, False) if idx!= M else (i, True) for idx, i in enumerate(importance)]
    cnt =1
  
    while importance:
        p = priority.pop(0)
        while importance[0][0] != p:
            importance.append(importance.pop(0))
            
        i = importance.pop(0)
        if i[1]:
            print(cnt)
            break
        else:
            cnt +=1