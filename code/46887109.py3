import sys

n = int(sys.stdin.readline())

for _ in range(n):
    doc_cnt, target = map(int,sys.stdin.readline().split())
    doc_list = list(enumerate(map(int, sys.stdin.readline().split())))
    priority_list = [doc_list[i][1] for i in range(doc_cnt)]
    answer = 0

    while True:
        if priority_list[0] == max(priority_list):
            answer += 1
            if doc_list[0][0] == target:
                print(answer)
                break
            else:                
                priority_list.pop(0)
                doc_list.pop(0)
        else:
            priority_list.append(priority_list.pop(0))
            doc_list.append(doc_list.pop(0))