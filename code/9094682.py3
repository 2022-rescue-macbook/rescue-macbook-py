import sys

def impl(ln,b,want):
    count = 0
    while b:
        if want == ln - len(b) and max(b) ==b[0]:
            count+=1
            break
        elif b[0] == max(b):
            b.pop(0)
            count+=1
        else:
            if want == ln - len(b):
                want = ln -1
            else:
                want-=1
            b.append(b.pop(0))
    
    return count

c = int(sys.stdin.readline().strip())

re =[]
for x in range(c):
    i = sys.stdin.readline().strip()

    ii = i.split()

    ln =int(ii[0])
    want = int(ii[1])

    i2 = sys.stdin.readline().strip()

    imp =i2.split()

    b = [int(imp[x]) for x in range(ln)]

    
    re.append(impl(ln,b,want))

for x in re:
    print(x)
    







    
