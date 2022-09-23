TestCase = int(input())

for _ in range(TestCase):
    N, T = list(map(int, input().split()))
    imp_list = list(map(int, input().split()))
    chk_list = [0 for _ in range(N)]
    chk_list[T] = "Target"
    result = 0

    while True:
        if imp_list[0] == max(imp_list):
            result += 1
            if chk_list[0] == "Target":
                print(result)
                break
            else:
                imp_list.pop(0)
                chk_list.pop(0)
        else:
            imp_list.append(imp_list.pop(0))
            chk_list.append(chk_list.pop(0))