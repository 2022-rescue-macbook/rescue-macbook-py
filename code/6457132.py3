for i in range(int(input())):
    p,q=map(int,input().split())
    lst=list(map(int,input().split()))
    lst[q]=float(lst[q])
    ord=0
    while True:
        while True:
            temp=lst[0]
            done=True
            for j in lst:
                if j>temp:
                    lst.append(temp)
                    del lst[0]
                    done = False
                    break
            if done==True:
                break
        del lst[0]
        ord+=1
        if type(temp)==float:
            print(ord)
            break
