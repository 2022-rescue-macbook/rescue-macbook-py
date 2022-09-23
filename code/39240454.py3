def printer(N, M, imp_list):
    value_list = list(range(1, N+1))
    M += 1
    cnt = 0
    while True:
        max_index = imp_list.index(max(imp_list))
        imp_list = imp_list[max_index:] + imp_list[:max_index]
        value_list = value_list[max_index:] + value_list[:max_index]
        imp_list.pop(0)
        printed = value_list.pop(0)
        cnt += 1
        if printed == M:
            return cnt


print_list = []
total = int(input())
for i in range(total):
    N, M = map(int, input().split())
    imp_list = list(map(int, input().split()))
    print_list.append(printer(N, M, imp_list))

for i in print_list:
    print(i)