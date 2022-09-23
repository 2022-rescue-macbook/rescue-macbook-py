import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):

    doc_num, doc_index = map(int, input().split())
    ip = list(map(int, input().split()))

    order = 1

    while True:
        if ip[0] == max(ip):
            if doc_index == ip.index(max(ip)):
                print(order)
                break
            else:
                ip.pop(0)
                order += 1
                doc_index -= 1
        
        else:
            a = ip.pop(0)
            ip.append(a)
            doc_index -= 1
        
        if doc_index < 0:
            doc_index += len(ip)