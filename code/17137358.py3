def printer(location, data):
    index = list(range(0, len(data)))
    count = 1
    
    while True:
        max_importance = max(data)
        if data[0] != max_importance:
            data.append(data.pop(0))
            index.append(index.pop(0))
            
        elif data[0] == max_importance:
            if index[0] == location:
                print(count)
                break
            else:
                data.pop(0)
                index.pop(0)
                count += 1
                
samples = int(input())
for ha in range(samples):
    
    length, location = list(map(int, input().split(' ')))
    data = list(map(int, input().split(' ')))
    printer(location, data)