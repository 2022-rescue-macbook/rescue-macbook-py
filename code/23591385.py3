# priority 1-9 : 9 Highest
import sys


cases = int(sys.stdin.readline())

for case in range(cases):
    time = 0
    front = 0

    n, m = map(int, sys.stdin.readline().split())
    # n : queue에 있는 job 의 수
    # m : 내 job 의 position

    priorities = list(map(int, sys.stdin.readline().split()))

    arr = [0]*10

    for p in priorities:
        arr[p] += 1

    while True:
        # 가장 우선순위 job의 priority 구함
        for j in range(len(arr))[::-1]:
            if arr[j] != 0:
                max_p = j
                break

        # print? or requeue?
        # print 시 소요시간 +1
        pf = priorities[front]
        if pf != -1:
            if max_p == pf:
                time += 1
                arr[pf] -= 1
                priorities[front] = -1
                if front == m:
                    break
        front = (front+1) % n
            # 현재 print 된 일의 순번이 내 일인지 확인

    print(time)



