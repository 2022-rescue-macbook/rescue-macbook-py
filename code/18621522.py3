T = int(input())

for _ in range(T):
    # N : 문서의 수
    # M : 궁금한 문서의 현재 위치
    N, M = map(int, input().split())
    I = list(map(int, input().split()))
    
    print_list = []
    for i in range(N):
        print_list.append([I[i], i])
    
    count = 0
    while True:
        temp_document = print_list.pop(0)
        important_number = temp_document[0]
        result = False
        for document in print_list:
            if document[0] > important_number:
                print_list.append(temp_document)
                result = True
                break
            
        if result:
            continue
        count += 1
        
        if temp_document[1] == M:
            print(count)
            break
                