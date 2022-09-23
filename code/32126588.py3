"""Solution code for "BOJ 1966. 프린터 큐".

- Problem link: https://www.acmicpc.net/problem/1966
- Solution link: http://www.teferi.net/ps/problems/boj/1966
"""

import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        def dist_from_last_index(index):
            dist = index - last_index
            return dist if dist >= 0 else dist + N

        N, M = [int(x) for x in sys.stdin.readline().split()]
        priorities = [int(x) for x in sys.stdin.readline().split()]
        max_priority = max(priorities)

        indexes_by_priority = [[] for _ in range(max_priority + 1)]
        for i, p in enumerate(priorities):
            indexes_by_priority[p].append(i)

        last_index = 0
        answer = 0
        for p in range(max_priority, priorities[M], -1):
            if not (indexes := indexes_by_priority[p]):
                continue
            answer += len(indexes)
            last_index = max(indexes, key=dist_from_last_index)
        target_dist = dist_from_last_index(M)
        answer += sum(1 for i in indexes_by_priority[priorities[M]]
                      if dist_from_last_index(i) <= target_dist)

        print(answer)


if __name__ == '__main__':
    main()
