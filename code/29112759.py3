#1966 프린터 큐
#큐의 성질은 FIFO라는 사실을 이용하고, 똑같은 INDEX의 리스트를 활용해서 사용함.(딕셔너리는 순서가 없어 활용 불가)
import sys
N = int(sys.stdin.readline())
for i in range(N):
    K, M = map(int, sys.stdin.readline().split())
    pr = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(pr)))
    order = 0
    while True:
        if pr[0] == max(pr):
            order += 1
            if idx[0] == M:
                break
            else:
                pr.pop(0)
                idx.pop(0)
        else:
            pr.append(pr.pop(0))
            idx.append(idx.pop(0))
    print(order)