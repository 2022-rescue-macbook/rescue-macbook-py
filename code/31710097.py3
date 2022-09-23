"""Solution code for "BOJ 1966. 프린터 큐".

- Problem link: https://www.acmicpc.net/problem/1966
- Solution link: http://www.teferi.net/ps/problems/boj/1966

"""

import sys

def main():
    n_testcase = int(sys.stdin.readline())
    
    for _ in range(n_testcase):
        n, m = tuple(map(int, sys.stdin.readline().split(' ')))
        priority_list = list(map(int, sys.stdin.readline().split(' ')))

        priority_count = [0 for i in range(10)]
        print_count = 0
        print_more = True

        for p in priority_list:
            priority_count[p] += 1

        highest_priority = max([p for p in range(10) if priority_count[p] > 0])

        while print_more:
            for i in range(len(priority_list)):
                if priority_list[i] == 0:
                    continue
                if priority_list[i] == highest_priority:
                    print_count += 1

                    if i == m:
                        print_more = False
                        break

                    priority_list[i] = 0
                    priority_count[highest_priority] -= 1
                    if priority_count[highest_priority] == 0:
                        highest_priority = max([p for p in range(10) if priority_count[p] > 0])
        print(print_count)


if __name__ == '__main__':
    main()