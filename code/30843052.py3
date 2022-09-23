def solution(importance, locations):

    # 제일 큰 값만 기억해
    cache = max(importance)

    turn = 0

    while True:
        elm = importance[0]
        loc = locations[0]
        if cache > elm:
            importance.append(importance.pop(0))
            locations.append(locations.pop(0))
        else:
            turn += 1
            if loc == M:
                return print(turn)
            importance.pop(0)
            locations.pop(0)
            # 제일 큰 값 교체
            cache = max(importance)


import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 가중치 리스트
    IMP = []
    IMP = list(map(int, input().split()))
    # 위치추적 리스트
    LOCS = [i for i in range(N)]
    solution(IMP,LOCS)