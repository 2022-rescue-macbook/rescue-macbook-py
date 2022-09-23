"""
1. 테스트 케이스 수 받기
2. 테스트 케이스 입력 2줄받기
3. Split하여 N, M int로 추출
4. Split하여 N개의 문서 중요도값 리스트 Qlist[int]로 추출
5. 궁금한 문서의 위치를 추적할 trace int 변수 생성
6. trace = N
7. Qlist의 index 0의 중요도와 Qlist Max값과 비교한다.
8. index 0이 크다면 trace값과 같은지 비교한다.
8-1. 같다면 trace출력하고 종료
8-2. 다르다면 궁금한 문서가 아니므로 pop하고 trace -1한다.
9. index 0이 작다면 trace값과 같은지 비교한다
9-1. 같다면 index 0을 pop하고 Qlist에 다시 Push한다. trace = 문서총갯수 -1
9-2. 다르다면 index 0을 pop하고 Qlist에 다시 Push한다. trace -1한다.
"""

case = int(input())

for _ in range(case):
    M, N = input().split()
    M = int(M)
    N = int(N)
    Qlist = list(input().split())

    trace = N
    Max = max(Qlist)

    count = 1

    while True:
        if Qlist[0] >= Max:
            if trace == 0:
                print(count)
                break
            else:
                pop = Qlist.pop(0)
                Max = max(Qlist)
                trace -= 1
                count += 1

        else:
            if trace == 0:
                pop = Qlist.pop(0)
                Qlist.append(pop)
                trace = len(Qlist) -1
            else:
                pop = Qlist.pop(0)
                Qlist.append(pop)
                trace -= 1