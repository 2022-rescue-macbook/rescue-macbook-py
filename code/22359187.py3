test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    imp_list = list(map(int, input().split()))
    sample_list = list(i for i in range(n))
    target_el = sample_list[m]    
    cnt = 0
    while True:
      if imp_list[0] == max(imp_list):
          cnt += 1
          if sample_list[0] == target_el:
              print(cnt)
              break
          else:
              imp_list.pop(0)
              sample_list.pop(0)
      else:
          imp_list.append(imp_list.pop(0))
          sample_list.append(sample_list.pop(0))