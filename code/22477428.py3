import sys


#sys.stdin = open('input.txt', 'r')

case = int(input())

for x in range(case):
    n,m = list(map(int, input().split(' ')))
    data = list(map(int, input().split(' ')))
    reverse = sorted(data,reverse=True)
    count = 0
    while data:
        tmp = data.pop(0)
        if tmp == reverse[0]:
            reverse.pop(0)
            count+=1
            if m==0:
                break
            else:
                m-=1
                
        else:
            data.append(tmp)
            if m == 0:
                m = len(data)-1
            else:
                m-=1
    print(count)