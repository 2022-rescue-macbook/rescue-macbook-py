import sys


T = int(sys.stdin.readline().rstrip())
N = []
M = []
DOC_INDEX = []
PRIORITY = []
answer = [0]*T

for i in range(0, T):
    N_M = sys.stdin.readline().rstrip().split()
    N.append(int(N_M[0]))
    M.append(int(N_M[1]))
    DOC_INDEX.append([j for j in range(0, N[i])])
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    PRIORITY.append(p)

for i in range(0, T):
    printed_no = 0
    target_index = DOC_INDEX[i][M[i]]
    P_LEN = N[i]
    while PRIORITY[i]:
        rearranged = False
        for j in range(1, P_LEN):
            if PRIORITY[i][0] < PRIORITY[i][j]:
                PRIORITY[i].append(PRIORITY[i][0])
                DOC_INDEX[i].append(DOC_INDEX[i][0])
                del (PRIORITY[i][0])
                del (DOC_INDEX[i][0])
                rearranged = True
                break
        if not rearranged:
            printed_no += 1
            P_LEN -= 1
            if DOC_INDEX[i][0] == target_index:
                answer[i] = printed_no
                break
            del (PRIORITY[i][0])
            del (DOC_INDEX[i][0])

for a in answer:
    print(a)
