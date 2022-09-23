import sys
input = sys.stdin.readline
for T in range(int(input())):
    N, M = map(int, input().split())
    target = list(map(int, input().split()))
    cnt = 0
    i = 0
    while len(target) != 0:
        if target[i] == max(target):      # 우선순위가 같음
            cnt += 1                      # 카운팅
            if i == M:                    # 인덱스도 같으면 break
                break
            if i == len(target) - 1:
                target.pop(i)
                i = 0
            else:
                target.pop(i)
                if i < M:
                    M -= 1
            N -= 1
        else:
            i = (i+1) % N

    print(cnt)