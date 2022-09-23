import sys
testcase = int(input())
for q in range(testcase):
    n,m = sys.stdin.readline().split()
    imp = sys.stdin.readline().split()
    for i in range(len(imp)):
        imp[i] = int(imp[i])
    impar = sorted(list(set(imp)))
    impar.reverse()
    m = int(m)

    count = 0
    jfix = 0
    for i in range(impar.index(imp[m])+1):
        for j in range(jfix, jfix + len(imp)):
            if imp[j%len(imp)] == impar[i]:
                count += 1
                jfix = j
                if j%len(imp) == m:
                    print(count)
                    break