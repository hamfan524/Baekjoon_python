import bisect
import sys
input = sys.stdin.readline

def lis(arr):
  lis_arr = [arr[0]]
  res = [0]
  for i in arr[1:]:
    if lis_arr[-1] < i:
      lis_arr.append(i)
      res.append(len(lis_arr) - 1)
    else:
      where = bisect.bisect_left(lis_arr, i)
      lis_arr[where] = i
      res.append(where)

  a = len(lis_arr)
  print(a)
  ans = []
  for i in range(len(res) -1, -1, -1):
    if res[i] == a - 1:
      ans.append(arr[i])
      a -= 1
  print(*ans[::-1])

input()
lis(list(map(int, input().split())))