test_case = int(input())

for case in range(test_case) :
    N, M = list(map(int, input().split(' ')))
    docs_val = list(map(int, input().split(' ')))
    docs_idx = [i for i in range(N)]
    cnt = 0
#    print("Printer queue :" ,docs_val)
    while len(docs_idx) > 0 :
        while docs_val[0] != max(docs_val) :
            temp = docs_val.pop(0)
            docs_val.append(temp)
            temp = docs_idx.pop(0)
            docs_idx.append(temp)

#        print("The %d-th doc printed.(priority : %d), queue : " % (docs_idx[0], docs_val[0]),docs_val)
        docs_val.pop(0)
        temp = docs_idx.pop(0)
        cnt += 1
        if temp == M :
            break

    print(cnt)