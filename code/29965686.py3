import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n,m = map(int,sys.stdin.readline().split())
    priority = list(map(int,sys.stdin.readline().split()))  #문서 중요도를 리스트에 담는다
    answer = 0

    while True:
        if priority[0] != max(priority):    #첫 문서의 중요도가 가장 높지 않다면
            priority.append(priority[0])    #첫 문서를 맨뒤로 옮긴다
            priority.remove(priority[0])    #첫 문서 삭제
            
            if m != 0:      #인덱스 값 이동
                m -= 1
            else:
                m = len(priority)-1

        elif priority[0] == max(priority):  #첫 문서가 중요도가 가장 높다면
            priority.remove(priority[0])    #첫 문서삭제
            answer += 1 #출력 순서 증가
            if m == 0:  #확인하고 싶은게 출력된다면, 반복문 탈출
                break
            m -= 1

    print(answer)    