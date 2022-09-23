#-*- encoding: utf-8 -*-
import sys
input = sys.stdin.readline

t = int(input().rstrip())
answer = []
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    data = list(map(int, input().rstrip().split()))
    idx = list(range(len(data))) #데이터들의 위치를 저장해둘 리스트
    #print(idx)
    target = idx[m]
    #print(target)
    cnt = 0
    while True:
        if data[0]==max(data):
            cnt+=1

            if idx[0] == target:
                print(cnt)
                break

            else:
                data.pop(0)
                idx.pop(0)
        else:
            data.append(data[0])
            data.pop(0)

            idx.append(idx[0])
            idx.pop(0)