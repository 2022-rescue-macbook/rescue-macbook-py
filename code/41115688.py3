import sys
testcase = int(input())
for _ in range(testcase):
    # 각 테스트케이스 실행
    N, M = map(int, sys.stdin.readline().split())
    que = list(sys.stdin.readline().split())
    cnt = 0
    while True:
        # 맨앞 값이 가장 큰 값이라면, 그냥 pop
        if que[0]==max(que):
            cnt += 1
            que.pop(0)
            # 위치 M 업데이트
            if M==0:
                print(cnt)
                break
            else: M -= 1
        # 더 큰 값이 뒤에 존재한다면, pop 후 append
        else:
            que.append(que.pop(0))
            # 위치 M 업데이트
            if M == 0:  M = len(que)-1
            else:       M -= 1