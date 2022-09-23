from sys import stdin
from collections import deque


class Solution:

    def __init__(self, n, m, p):
        self.N = n
        self.M = m
        self.P = p

    def get_answer(self):
        que = deque((i, self.P[i]) for i in range(self.N))
        c = 0
        self.P.sort()
        max_i = self.N - 1
        while que:
            top = que[0]
            if top[1] != self.P[max_i]:
                que.rotate(-1)
                continue
            max_i -= 1
            que.popleft()
            c += 1
            if top[0] == self.M:
                break
        print(c)


if __name__ == "__main__":
    T = int(stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, stdin.readline().rstrip().split())
        P = list(map(int, stdin.readline().rstrip().split()))
        s = Solution(N, M, P)
        s.get_answer()
