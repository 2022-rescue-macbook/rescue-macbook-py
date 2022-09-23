"""from collections import deque
t = int(input()) # 1 2 3 4 m=2
global l
def sorting(it):
    it.sort()
    l = deque()
    s = it[::-1]
    for i in s:
        l.append(i)
    return l # 4 3 2 1



for _ in range(t):
    n, m = map(int, input().split())
    it = list(map(int, input().split()))
    if len(it) == 1:
        print(1)
    else:
        check = sorting(it)
        cnt = 0
        while True:
            a = check.popleft()

            if it.index(a) == m:
                cnt += 1
                break
            else:
                cnt += 1

        print(cnt)
deque를 활용해서 구현을 해보았다.
우선, 중요도가 1개라는 뜻은 문서가 1개라는 의미이므로 이때는 1을 출력하면 된다.
그렇지 않을 경우, 데이터를 뺄 deque와 중요도 리스트를 만든다.
왜냐하면, deque를 내림차순으로 정렬후 popleft를 한 값의 '중요도리스트의 인덱스'가 m과 같다면
count 를 1하나씩 더해가며 count를 바로 출력하면 된다.
(popleft = m의 의미는 출력하고자 하는 문서의 출력순서이다.)

위 코드에서 하나 빠진 것이 있는데, 바로 '중복되는 중요도'가 오는 경우이다.
사실 이는 간단하게 해결할수있다.
중복 정렬을 해결하는 함수를 정의하고, '재귀함수'를 통해 0.001씩 더해주면 된다.
ex) 1 1 9 1 1 1
1.001 1.002 9 1.003 1.004 1.005
set_sorting()(임의로 함수이름 정의) ==> 9 1.005 1.004 1.003 1.002 1.001
이러면 알고리즘 구현방식의 핵심인 '인덱스'비교가 가능해진다.
허나, 귀찮아서 dp와 같은 개념으로 중복경우까지 포함되는 코드 구현을 해보았다.
알고리즘의 핵심인 인덱스비교는 동일하다.

알고리즘 구현 방식:
1. 기존 중요도 리스트 생성 및 비교할 중요도 리스트 생성
2. deque의 역할을 할 judge 리스트 생성
3. judge에서 m번째 인덱스에 해당되는 값만 'T'로 바꿔줌.
4. 중요도 리스트의 0번째 인덱스가 중요도 리스트의 최댓값이라는 뜻은 정렬 완료됬다는 것.
4-1. 이때는 count를 하나씩 더해가는데 judge의 첫번째가 'T'가 될떄까지
    왼쪽 값을 pop해줌 (==> pop(0) deque에서 popleft()에 해당.)
    첫번쨰가 T가 되면 바로 count 프린트.
5. 정렬이 안됬다면 (= imp[0] != max(imp)), imp와judge popleft() 해줌.
"""
t = int(input())
for _ in range(t):
    nm = list(map(int,input().split(' ')))
    n = nm[0]
    m = nm[1]
    imp = list(map(int,input().split(' ')))
    judge = [0 for _ in range(n)]
    judge[m] = 'T'
    cnt = 0
    if len(imp) == n:
        while True:
            if imp[0] == max(imp):
                cnt += 1
                if judge[0] == 'T':
                    print(cnt)
                    break
                else:
                    imp.pop(0)
                    judge.pop(0)
            else:
                imp.append(imp.pop(0))
                judge.append(judge.pop(0))