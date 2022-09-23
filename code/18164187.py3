def operate():
    count=0
    while True:
        if max(priority)==priority[0]:
            if check[0]==True:
                break
            priority.pop(0)
            check.pop(0)
            count+=1
        else:
            priority.append(priority.pop(0))
            check.append((check.pop(0)))
    print(count+1)


if __name__ == '__main__':
    T=int(input())
    for test_case in range(1, T+1):
        query=list(map( int, input().split()))
        priority=list(map(int, input().split()))
        check=[False for _ in range(query[0])]
        check[query[1]]=True
        operate()
