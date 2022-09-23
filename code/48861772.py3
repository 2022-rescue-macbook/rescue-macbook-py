import sys

case_number = int(sys.stdin.readline())

for i in range(case_number):
    job_number, position = map(int, sys.stdin.readline().split())
    priorities = ''.join(sys.stdin.readline().split())
    my_priority = int(priorities[position])
    higher_than_me = sorted(set(_ for _ in priorities if int(_) > my_priority), reverse=True)
    consumed_time = 0
    point = 101

    if higher_than_me:
        for j in higher_than_me:
            faster = [_ for _ in enumerate(priorities) if _[1] == j]
            consumed_time += len(faster)
            setting = [tu for tu in faster if tu[0] < point]
            if setting: point = int(setting[-1][0])
            else: point = faster[-1][0]

    same_priority = [_ for _ in enumerate(priorities) if _[1] == priorities[position]]

    if point < position:
        for x in same_priority:
            if point < x[0] <= position: consumed_time += 1
    else:
        for x in same_priority:
            if point < x[0] or x[0] <= position: consumed_time += 1

    print(consumed_time)
