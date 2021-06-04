import bisect
import sys
input = sys.stdin.readline

def lis(arr):
  lis_arr = [arr[0]]
  for i in arr[1:]:
    if lis_arr[-1] < i:
      lis_arr.append(i)
    else:
      where = bisect.bisect_left(lis_arr, i)
      lis_arr[where] = i
  
  a = len(lis_arr)
  print(a)

input()
lis(list(map(int, input().split())))