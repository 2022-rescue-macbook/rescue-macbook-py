T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    weight_list = list(map(int, input().split()))
    res_list = list(range(N))
    res_list[M] = 'target'

    order = 0

    while True :
        if weight_list[0] == max(weight_list):
            order += 1
            if res_list[0] == 'target' :
                print(order)
                break
            else :
                weight_list.pop(0)
                res_list.pop(0)
        else :
            weight_list.append(weight_list.pop(0))
            res_list.append(res_list.pop(0))