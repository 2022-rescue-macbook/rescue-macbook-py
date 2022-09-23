import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    # idx 변수 생성: 문서마다 고유 인덱스를 생성
    idx = list(range(len(imp)))
    # m번째 인덱스를 target으로 둠
    idx[m] = 'target'

    # order 초기화(순서)
    order = 0

    # while True이므로 무한 반복인데 break가 있기 때문에 if절에 걸리는 조건이 맞으면 반복이 중단된다.
    while True:
         # 만약 imp의 첫 번째 값이 가장 크다면 order를 하나 증가시킨다.
        if imp[0]==max(imp):
            order += 1
                        
            # idx의 첫 번째 값이 target이라면
            if idx[0]=='target':
                # order를 출력하고 반복을 중단한다.
                print(order)
                break
            # 그렇지 않다면 imp와 idx의 첫 번째 값을 제거한다.
            else:
                imp.pop(0)
                idx.pop(0)

         # idx의 첫번째 값이 target이 될 때까지 반복된다.
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))  