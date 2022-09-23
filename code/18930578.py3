from sys import stdin

case = int(stdin.readline())

for c in range(case):
    docu_count, target_inx = [int(i) for i in stdin.readline().split()]
    documents = [int(i) for i in stdin.readline().split()]
    p_num = 0
    while len(documents) != 0:
        p = documents.pop(0)
        for d in documents:
            if p < d:
                documents.append(p)
                if target_inx == 0:
                    target_inx = len(documents) - 1
                else:
                    target_inx -= 1
                break
        else:
            p_num += 1
            if target_inx == 0:
                print(p_num)
                break
            else:
                target_inx -= 1
