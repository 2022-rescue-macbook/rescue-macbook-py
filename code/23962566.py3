test_case=int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split()))
    imp=list(map(int, input().split()))
    lst=list(range(len(imp)))
    lst[m]='a'

    count=0

    while True:
        
        if imp[0]==max(imp):
            count+=1
            
            if lst[0]=='a':
                print(count)
                break
            else:
                imp.pop(0)
                lst.pop(0)
        else:
            imp.append(imp.pop(0))
            lst.append(lst.pop(0))