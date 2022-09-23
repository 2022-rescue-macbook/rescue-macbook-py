import sys

def printer_q(N, M):
    cnt = 0

    while True:
        cnt += 1    # 한번 돌아가기 시작
        document = documents.pop(0)
        M -= 1
        if len(documents) == 0:    # 큐 길이가 0 -> 문서 출력 끝!
            return cnt
        N -= 1    # 문서를 하나 pop 했으므로 전체 문서 개수 -1

        # 문서 중요도 확인을 위한 반복문
        for n in range(N):
            if document < documents[n]:    # 중요도가 더 높은 것이 있다?
                documents.append(document)    # 문서 제일 뒤로
                cnt -= 1
                if M == -1:    # 문서 위치가 0 -> 제일 끝으로 변경
                    M = N
                N += 1    # 제일 뒤로 문서 이동한 것이므로 문서 개수 +1
                break

        if M == -1:
            return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().split()))
    print(printer_q(N, M))