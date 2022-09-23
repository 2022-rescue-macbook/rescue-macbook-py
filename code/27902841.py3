t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    que = list([0 for _ in range(n)])
    count = 0  # 출력값을 저장하는 변수
    que[m] = 1  # 궁금한 문서 위치 저장

    while True:
        if priority[0] == max(priority): # priority의 첫번째 요소가 최대중요도
            count += 1  # count 1 증가

            if que[0] != 1: # 최대 중요도이지만 우리가 찾고자 하는 값이 아님
                que.pop(0)  # 큐에서 뺌
                priority.pop(0) # 우선순위 리스트에서도 뺌
            else: # 최대 중요도이고 우리가 찾고자 하는 값임
                print(count) #출력
                break # 종료
        else: # 최대 중요도가 아닐 때
            priority.append(priority.pop(0)) # 중요도 리스트에서 빼서 뒤로 보냄
            que.append(que.pop(0))  # 큐에서도 빼내고 뒤로 보냄


