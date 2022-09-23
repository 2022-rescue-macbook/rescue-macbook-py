import sys

T = int(sys.stdin.readline())

for _ in range(T):
    # x는 프린터 기기로 인쇄할 문서 개수
    # y는 궁금한 문서의 위치
    x, y = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    order = 0

    while 1:
        if imp[0] == max(imp):
            order += 1
            if y == 0:
                print(order)
                break
            else:
                y -= 1
                imp.pop(0)
        else:
            imp.append(imp[0])
            imp.pop(0)
            if y <= 0:
                y = len(imp)-1
            else:
                y -= 1
