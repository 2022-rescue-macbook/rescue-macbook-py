
num = int(input())


for i in range(num):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))

    target = [1 if i==m else 0 for i in range(n)]
    count = 0

    while(True):
        
        if imp[0]  == max(imp):
            count +=1
            if target[0] == 1:
                print(count)
                break
            else:
                del imp[0]
                del target[0]
        else:
            imp.append(imp[0])
            del imp[0]
            target.append(target[0])
            del target[0]