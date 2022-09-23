import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    nmLst = []
    ipLst = []

    for _ in range(t):
        nm = []
        n, m = map(int, sys.stdin.readline().strip().split())
        nm.append(n)
        nm.append(m)
        nmLst.append(nm)

        ip = list(map(int, sys.stdin.readline().strip().split()))
        ipLst.append(ip)

    for i in range(t):
        lst1 = ipLst[i]
        lst2 = []
        locate = int(nmLst[i][1])

        while 1:
            if lst1[0] == max(lst1): #맨앞이 제일 클 때
                tmp = lst1[0]
                del lst1[0]
                lst2.append(tmp)
                locate -= 1
                if locate == -1:
                    print(len(lst2))
                    break

            else: #맨앞이 제일 크지 않을 때
                tmp = lst1[0]
                del lst1[0]
                lst1.append(tmp)
                locate -= 1
                if locate == -1:
                    locate = len(lst1) - 1
