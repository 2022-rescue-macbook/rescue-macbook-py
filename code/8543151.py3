case = int(input())
for i in range(case):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    
    count = 0
    temp = [0 for i in range(N)]
    temp[M] = 1
    while documents:
        loc = documents.index(max(documents))
        count += 1
        if temp[loc]==1:
            break
        if loc == len(documents)-1:
            documents = documents[:loc]
            temp = temp[:loc]
        else:
            documents =  documents[loc+1:]+documents[:loc]
            temp = temp[loc+1:]+temp[:loc]
    print(count)