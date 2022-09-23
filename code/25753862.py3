import sys

# test case input
T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    # N(1 ≤ N ≤ 100) : 문서의 개수,
    # M(0 ≤ M < N) : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수
    N, M = map(int, sys.stdin.readline().rstrip().split())

    # 문서 출력 수 세기
    count = 0

    # 문서 리스트
    doc_list = list(sys.stdin.readline().rstrip().split())

    while len(doc_list) != 0 :
        # 리스트에서 최우선 순위가 아니라면, 맨 뒤로 보냄
        if doc_list[0] != max(doc_list):
            doc_list.append(doc_list[0])
            del doc_list[0]
            # 최우선 순위가 아니므로 맨 뒤로감 따라서 M은 마지막번째로 바꿔줌
            if M == 0 :
                M += len(doc_list)-1
            # 그 외의 순서면 M을 한 칸씩 앞으로 땡긴다
            else :
                M -= 1
        # 리스트에서 최우선 순위라면
        else :
            del doc_list[0]
            count += 1
            if M == 0 :
                print(count)
                break
            else :
                M -= 1