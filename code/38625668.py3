import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))
    papers_target = papers[:]
    papers_target[M] = "target"
    res = 0

    while True:
        if papers[0] == max(papers):
            res += 1

            if papers_target[0] == "target":
                print(res)
                break
            else:
                del papers[0]
                del papers_target[0]

        else:
            papers.append(papers[0])
            del papers[0]

            papers_target.append(papers_target[0])
            del papers_target[0]