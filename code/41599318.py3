# 13 - 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys
input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    n, m = map(int, input().split())
    p = list(map(int,input().split()))
    
    target = [0] * n
    target[m] = 1
    
    res = 0
    
    while True:
        if p[0] == max(p):
            res += 1
            if target[0] == 1:
                print(res)
                break
            else:
                # 인쇄
                del p[0]
                del target[0]               
        else:
            p.append(p[0])
            target.append(target[0])
            del p[0]
            del target[0]