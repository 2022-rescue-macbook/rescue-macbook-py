import sys
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    n, m = map(int, input().split())
    queue = [*map(int, input().split())]
    max_num = max(queue)
    count = 0
    while True :
        if queue[0] < max_num :
            queue.append(queue.pop(0))
        else :
            # m이 첫번째 숫자인 경우 문제 해결
            count += 1
            if m == 0 :
                print(count)
                break
            queue.pop(0)
            # 큐에서 가장 우선순위가 높은 숫자를 갱신
            max_num = max(queue)
        # m의 순서를 옮김
        m = m - 1 if m > 0 else len(queue) - 1