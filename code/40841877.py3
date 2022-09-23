for i in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    paper = []
    dict = {}
    ans = a = 0
    
    for i in range(n):
        paper += [[lst[i], i]]
        
    lst.sort(reverse=True)
    
    for num in lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
        
    for num in dict.keys():
        while dict[num]:
            if paper[0][0] == num:
                ans += 1
                dict[num] -= 1
                if paper[0][1] == m:
                    a = ans
                paper.pop(0)
            else:
                paper += [paper.pop(0)]
                
    print(a)
    