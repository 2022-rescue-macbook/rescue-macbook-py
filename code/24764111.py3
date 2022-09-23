import operator
import sys

iteration = int(sys.stdin.readline().rstrip())

for i in range(iteration):
    N, M = map(int, sys.stdin.readline().rstrip().split())

    # 주어진 중요도 순 및 각 중요도의 위치, 현재 가리키고 있는 위치
    imp = list(map(int, sys.stdin.readline().rstrip().split()))
    loc = []
    for j in range(len(imp)):
        loc.append(j)
    pos = 0

    tmp = sorted(imp, reverse=True)
    tmp_pos = 0
    # 중요도 순으로 정리해둔 tmp 배열에서 중요도가 높은 것부터 하나씩 확인
    # imp, loc를 통해 tmp를 따라가면서 문제에서 주어진 M이 몇 번째인지 확인
    while True:
        if tmp[tmp_pos] == imp[pos]:
            imp[pos] = -1
            tmp_pos += 1
            if loc[pos] == M:
                break
        else:
            pos += 1
            pos %= N

    print(tmp_pos)