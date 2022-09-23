case = int(input())

for i in range(case) :
    a, b = map(int, input().split())
    count = 1
    
    lst = list(map(int, input().split()))

    while 1 :
        if lst[0] != max(lst) :
            lst.append(lst[0])
            lst.remove(lst[0])
            # count += 1
            if b == 0 :
                b = int(len(lst)-1)
                continue
            else :
                b -= 1
        else :
            if b == 0 :
                print(count)
                break
            else :
                lst.remove(lst[0])
                count += 1
                b -= 1
                
                
                    
            

    
