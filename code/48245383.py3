import sys
input = sys.stdin.readline

case_num = int(input())
ans_list = []
for i in range(case_num):
    N, M = map(int, input().split())
    importance_list = list(map(int, input().split()))
    importance_idx = [0 for _ in range(N)]
    importance_idx[M] = 1

    count = 0
    while True:
        if importance_list[0] == max(importance_list):
            count += 1
            if importance_idx[0] == 1:
                ans_list.append(count)
                break
            else:
                del importance_list[0]
                del importance_idx[0]
        else:
            importance_list.append(importance_list[0])
            del importance_list[0]
            importance_idx.append(importance_idx[0])
            del importance_idx[0]

for ans in ans_list:
    print(ans)