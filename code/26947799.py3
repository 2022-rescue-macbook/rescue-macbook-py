import sys

def main():

    case_count = int(sys.stdin.readline())
    cases = []
    for i in range(case_count):
        n, m = map(int, sys.stdin.readline().split())
        seq = list(map(int, sys.stdin.readline().split()))
        cases.append((m, seq))

    for case in cases:
        seq = [num for num in enumerate(case[1])]
        m = case[0]

        pop_counter = 0
        while(len(seq) > 0):
            appended = False
            k = seq.pop(0)

            for t in seq:
                if k[1] < t[1]:
                    appended = True
                    seq.append(k)
                    break

            if appended != True:
                pop_counter += 1

            if k[0] == m and appended == False:
                print(pop_counter)
                break
        

if __name__ == '__main__':
    main()
