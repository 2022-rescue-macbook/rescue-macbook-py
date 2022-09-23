from sys import stdin


def last_index(l, v):
    l.reverse()
    res = (len(l)-1) - l.index(v)
    l.reverse()
    return res


if __name__ == '__main__':
    num = int(stdin.readline())
    for _ in range(num):
        N, M = map(int, stdin.readline().split())
        priorities = list(map(int, stdin.readline().split()))
        cnt = 1

        while len(priorities) > 0:
            # print(priorities)
            # print("M : " + str(M))
            if priorities[0] < max(priorities):
                # swap
                if M == 0:
                    M = len(priorities)-1
                else:
                    M -= 1

                priorities.append(priorities[0])
                del priorities[0]
            else:
                # print
                if M == 0:
                    print(cnt)
                    break
                else:
                    del priorities[0]
                    cnt += 1
                    M -= 1
