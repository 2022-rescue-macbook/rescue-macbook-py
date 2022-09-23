testcase = int(input())

def test(a):
    for i in range(1, len(a)):
        if a[0] < a[i]:
            return 1
    return 0

def change():
    a.append( a.pop(0) )
    b.append( b.pop(0) )
    
for i in range(testcase):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    k = a[M]
    if len(a) == len(set(a)):
        a.sort()
        a.reverse()
        print(a.index(k)+1)
    else:
        b = [i for i in range(N)]
        s = 1
        while True:
            
            while (test(a) != 0):
                change()
                
            if b[0] == M:
                print(s)
                break
            
            a.pop(0)
            b.pop(0)
            s += 1