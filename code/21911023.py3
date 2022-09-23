import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    temp = sorted(arr, reverse= True)
    answer = 0
    idx = 0
    while True:
        for i,j in enumerate(arr): #정렬되지 않은 것
            first = temp[idx] #정렬된것의 첫번째부터
            if first == j: #우선순위 제일 높은 것이 j랑 동일하다면
                answer += 1
                idx += 1 # 다음것으로 진행
                if i == m:
                    break
        else:
            continue
        break
    print(answer)





