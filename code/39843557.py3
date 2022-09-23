test_case = int(input())
for i in range(test_case):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    base = data[M]
    data[M] = 0
    result = 0
    if len(data) != 1:
        for j in range(9):
            number = 9-j
            count_number = data.count(number)
            if count_number != 0 and number > base :
                for k in range(count_number):
                    num_index = data.index(number)
                    new_data = data[num_index:] + data[:num_index]
                    new_data.pop(0)
                    result += 1
                    data = new_data                   
            elif number == base :
                for k in range(1,base):
                    count_number2 = data.count(k)
                    if count_number2 != 0:
                        for l in range(count_number2):
                            data.remove(k)
                result = result + 1 + data.index(0)
                print(result)
                break
                
                  
    else: print(1)
        
            
            
        
    
    
    