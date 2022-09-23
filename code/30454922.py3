import sys

input = sys.stdin.readline


def sol1966():
    answer = []
    for t in range(int(input())):
        n, m = map(int, input().split())
        docs = [*map(int, input().split())]
        turn = 1
        while True:
            i = docs.index(max(docs))
            if i == m:
                break
            docs = docs[i+1:] + docs[:i]
            m = m-i-1 if i < m else len(docs)-i+m
            turn += 1
        answer.append(str(turn))
    print('\n'.join(answer))
                

if __name__ == '__main__':
    sol1966()