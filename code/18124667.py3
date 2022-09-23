import sys

t = int(sys.stdin.readline())

# 인쇄 : queue의 top을 pop

for _ in range(t):

    n, m = map(int, sys.stdin.readline().split())
    papers = [int(i) for i in sys.stdin.readline().split()]

    front = 0 # top의 위치
    back = n-1 # back의 위치
    pop_idx = None # pop할 때의 index : if 조건이 만족되지 않을 때 top을 pop한다.
    flag_idx = m # 문제에서 찾으라고 한 기준 index
    cnt = 0 # pop한 횟수 = 인쇄 횟수

    if n == 1:
        print(1)
    else:
        while pop_idx != flag_idx:
            if any(paper > papers[front] for paper in papers[front+1:]): # front 뒤에 애가 하나라도 크다면
                papers.append(papers[front]) # top을 뒤로 보냄.
                front += 1
                back += 1
                if front - 1 == flag_idx: # 찾아야 할 flag가 top에 있었고, 뒤로 밀렸다면,
                    flag_idx = back # flag의 index도 변함.
            else: # front 뒤에 큰 애가 없다 = 인쇄한다면,
                pop_idx = front # top을 pop
                front += 1 # front의 위치만 +1
                cnt += 1
        print(cnt)