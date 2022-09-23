t = int(input())
target = 0
for _ in range(t):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    cnt = 0
    
    while m != -1:
        if n_list[0] == max(n_list):
            n_list.pop(0)
            m -= 1
            cnt += 1
        else:
            n_list.append(n_list.pop(0))
            
            if m == 0:
                m = len(n_list) - 1
            else:
                m -= 1
    print(cnt)