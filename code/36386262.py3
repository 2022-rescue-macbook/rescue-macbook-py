from sys import stdin

input = lambda : stdin.readline().rstrip()

def main():
    n = int(input())
    for _ in range(n):
        n_docs, highlight = map(int, input().split())
        docs = list(map(int, input().split()))
        print(sol(n_docs, highlight, docs))
    return

def sol(n_docs, highlight, docs):
    ans = 0
    while True:
        tray = docs[0]
        if max(docs) > tray:
            docs.pop(0)
            docs.append(tray)
            if highlight == 0:
                highlight = len(docs)
        else:
            docs.pop(0)
            ans += 1
            if highlight == 0:
                return ans
        highlight -= 1

if __name__ == "__main__":
    main()