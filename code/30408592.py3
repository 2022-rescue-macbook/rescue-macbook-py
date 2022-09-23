test_case = int(input())

for _ in range(test_case):
    n,m = map(int,input().split())
    imp = list(map(int,input().split()))
    
    cnt = 0
    max_imp = max(imp)
    while True:
        job = imp.pop(0)
        m -= 1
        if job == max_imp:
            cnt +=1
            if m == -1:
                print(cnt)
                break
            max_imp=max(imp)
        else:
            if m == -1:
                m = len(imp)
            imp.append(job)