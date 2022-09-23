#12.01 백준 - 프린터 큐
def queue(l,num):
    count = 1
    while True:
        if num == 0:
            if l[num] == max(l):
                return count
            else:
                l.append(l.pop(0))
                num = len(l)-1
        elif l[0] == max(l):
            l.pop(0)
            num -= 1
            count += 1
        else:
            l.append(l.pop(0))
            num -= 1

T=int(input())
for _ in range(T):
    n,num = map(int,input().split())
    l=list(map(int,input().split()))
    print(queue(l,num))