import sys
input = sys.stdin.readline

n = int(input())

for __ in range(n):
    num, idx = map(int, input().split())
    n_list = list(map(int, input().split()))
    target_idx = list(range(num))
    target_idx[idx] = "!!!"
    count = 0
    while True:
        if n_list[0] == max(n_list):
            count +=1
            if target_idx[0] == "!!!":
                print(count)
                break
            else:
                n_list.pop(0)
                target_idx.pop(0)
        else:
            n_list.append(n_list[0])
            n_list.pop(0)
            target_idx.append(target_idx[0])
            target_idx.pop(0)