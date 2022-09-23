# testCase
T = int(input())

for _ in range(T):
    # doc number, importance
    N, M = map(int, input().split())

    # importance list
    ipt_list = list(map(int, input().split()))
    idx_list = list(range(len(ipt_list)))
    idx_list[M] = 'target'
    cnt = 0
    while True:
        if max(ipt_list) == ipt_list[0]:
            cnt += 1
            if idx_list[0] == 'target':
                print(cnt)
                break
            else:
                ipt_list.pop(0)
                idx_list.pop(0)
        else:
            ipt_list.append(ipt_list.pop(0))
            idx_list.append(idx_list.pop(0))