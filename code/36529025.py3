import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    imp_list = list(map(int,input().split()))
    cnt = 0
    doc = imp_list[m]
    imp_list[m] = 0
    while doc < max(imp_list):
        M = imp_list.index(max(imp_list))
        for _ in range(M):
            imp_list.append(imp_list.pop(0))
        imp_list.pop(0)
        cnt += 1
    while imp_list.count(doc) != 0:
        if imp_list.index(doc) < imp_list.index(0):   
            imp_list.remove(doc)
            cnt += 1
        else:
            break
    print(cnt+1)