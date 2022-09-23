T =int(input()) 

for i in range(T):
    a, b = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = [0]*a
    lst2[b] = 1
    
    cnt = 1
    
    while True:
        m = max(lst1)

        if lst1[0] == m and lst2[0] == 1:
            break
        elif lst1[0] == m and lst2[0] != 1:
            lst1.pop(0)
            lst2.pop(0)
            cnt += 1
        else:
            lst1.append(lst1.pop(0))
            lst2.append(lst2.pop(0))  

    print(cnt)