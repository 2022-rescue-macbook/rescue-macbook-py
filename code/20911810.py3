num = input() #Test Case
num = int(num)
for i in range(num):
    idx = []
    a,b  = input().split() #a = 문서 수, b = 몇 번째인지
    a = int(a)
    b = int(b)
    count = 0
    for j in range(a):
        idx.append(j)
    pro = list(map(int, input().split()))       
    while True:
        if pro[0] == max(pro): 
            count += 1 
            if idx[0] == b:
                print(count)
                break
            else:
                pro.pop(0)
                idx.pop(0)
        else:
            pro.append(pro.pop(0))
            idx.append(idx.pop(0))