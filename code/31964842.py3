import sys
input = sys.stdin.readline

if __name__=='__main__':
  tc = int(input())

  for i in range(tc):
    count = 1
    printer = True
    text_totalNum, text_index = map(int, input().split())
    text_list = list(map(int, input().split()))

    maxNum = max(text_list)

    while printer:
      if text_list[0] == maxNum and text_index == 0:
        printer = False
      elif text_list[0] == maxNum:
        text_list.pop(0)
        maxNum = max(text_list)
        text_totalNum -= 1
        text_index -= 1
        count += 1
      elif text_list[0] != maxNum:
        if text_index == 0:
          text_list.append(text_list.pop(0))
          text_index = text_totalNum - 1
        else:
          text_list.append(text_list.pop(0))
          text_index -= 1

    print(count)