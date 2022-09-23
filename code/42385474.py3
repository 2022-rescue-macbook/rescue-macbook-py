n = int(input())

ans = [0] * n
for i in range(n):
    num_p, key = map(int, input().split())
    printer = list(map(int, input().split()))

    cnt = 1

    while printer:
        #print(printer)
        tmp_p = printer.pop(0)
        if len(printer) == 0:
            break
        if max(printer) > tmp_p:
            printer.append(tmp_p)
            if key == 0:
                key = num_p -1
            else: 
                key -= 1
        else:
            if key == 0:
                break
            cnt += 1
            num_p -= 1
            key -= 1
        
    ans[i] = cnt 


for i in range(n):
    print(ans[i])