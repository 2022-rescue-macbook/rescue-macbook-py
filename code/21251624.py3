t = int(input())

for i in range(t):
    n, m = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    a_= [0 for i in range(n)]

    a_[m] = 1
    rank = 0

    while True:
        if a[0] == max(a):
            rank += 1
            if a_[0] == 1:
                break
            else:
                del a[0]
                del a_[0]
        else:
            a.append(a[0])
            del a[0]
            a_.append(a_[0])
            del a_[0]

    print(rank)