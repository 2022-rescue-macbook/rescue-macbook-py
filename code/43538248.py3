testCase = int(input())
for _ in range(testCase):
    level = 10
    document = 1
    printing = 0
    length, order = map(int, input().split())
    importance = list(map(int, input().split()))
    while importance[order] != 0 :
        level -= 1
        for k in range(printing, printing+length, 1):
            if importance[k%length] == level:
                importance[k%length] = 0
                if importance[order] != 0:
                    document +=1
                printing = k%length+1
    print(document)