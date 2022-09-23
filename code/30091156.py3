# 1966번: 프린터 큐

import sys

case = int(sys.stdin.readline()) # 테스트 케이스 개수
while case:
    order = 0 # 문서가 출력되는 순서
    count, index = map(int, sys.stdin.readline().split())
    # count = 문서 개수, target = 몇번째로 인쇄되었는지 찾아야하는 문서
    queue = list(map(int, sys.stdin.readline().split())) # 문서 중요도 입력받음
    tmplist = list(range(len(queue)))
    tmplist[index] = "target"
    target = queue[index]
    while True:
    # 중요도가 중복되는 문서들은 어떻게 해결할까??
        if queue[0] == max(queue):
            order += 1

            if tmplist[0] == "target":
                print(order)
                break
            else:
                queue.pop(0)
                tmplist.pop(0)
        else:
            queue.append(queue.pop(0))
            tmplist.append(tmplist.pop(0))
    case -= 1