'''
첫 줄에 test case의 수가 주어진다. 
각 test case에 대해서 문서의 수 N(100이하)와 
몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 어떤 위치에 있는지를 알려주는 M(0이상 N미만)이 주어진다. 

다음줄에 N개 문서의 중요도가 주어지는데, 
중요도는 1 이상 9 이하이다. 중요도가 같은 문서가 여러 개 있을 수도 있다. 위의 예는 N=4, M=0(A문서가 궁금하다면), 
중요도는 2 1 4 3이 된다.

3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
import sys
rnd = int(sys.stdin.readline())
sols = []
for _ in range(rnd):
    size, ni = map(int, sys.stdin.readline().split())
    ipts = list(map(int, sys.stdin.readline().split()))
    mirr = [i for i in range(len(ipts))]
    cnt = 1
    while 1 :
        tc = ipts.index(max(ipts))
        if mirr[tc] == ni :
            break
        i = 0
        while i < tc :
            ipts.append(ipts.pop(0))
            mirr.append(mirr.pop(0))
            i += 1
        ipts.pop(0)
        mirr.pop(0)
        cnt += 1
    sols.append(cnt)
print(*sols, sep='\n')