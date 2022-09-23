import sys

case = int(input())

def sol() :
    n, m = map(int, sys.stdin.readline().split())
    docu = list(map(int, sys.stdin.readline().split()))

    turn = 0
    ind = -1
    while True :
        ind = (ind + 1) % n
        if docu[ind] == max(docu) :
            docu[ind] = 0
            turn += 1
            if ind == m :
                return turn

solution = []

for i in range(case) :
    solution.append(sol())

for i in range(case) :
    print(solution[i])