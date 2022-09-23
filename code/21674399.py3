
test_case = int(input())
for i in range(test_case):
    a,b = map(int,input().split())
    inn = list(map(int,input().split()))
    comp = [0 for i in range(a)]  # 지정 값의 자리를 저장할 수 있는 list 필요
    comp[b] = 1
    count = 0
    while inn: 
        if inn[0] == max(inn):
            
            count+=1
            if comp[0] == 1:  
                print(count)
                break
            else:
                del inn[0]
                del comp[0]
            
        else:
            inn.append(inn[0])
            del inn[0]
            comp.append(comp[0])
            del comp[0]