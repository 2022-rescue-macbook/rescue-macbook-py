import sys

def ishigher(n,list_):
    for i in list_:
        if i > n:
            return True
    return False


for i in range(int(input())):
    N,M = map(int,input().split())
    stack = list(map(int,input().split()))
    index = [_ for _ in range(N)]
    cnt = 0
    while True:
        target = stack.pop(0)
        target_index = index.pop(0)
        if not ishigher(target,stack):
            cnt += 1
            if target_index == M:
                print(cnt)
                break
        else:
            stack.append(target)
            index.append(target_index)