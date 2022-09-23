num = int(input())

for _ in range(num):
    n,m = list(map(int, input().split()))
    n_li = list(map(int, input().split()))
    find = list(range(len(n_li)))
    find[m] = 'target'
    
    count = 0
    
    while True:
        if n_li[0] == max(n_li):
            count += 1
            
            if find[0] == 'target':
                print(count)
                break
            else:
                n_li.pop(0)
                find.pop(0)
        else:
            n_li.append(n_li.pop(0))
            find.append(find.pop(0))