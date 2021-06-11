import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def postorder(start, end):
  if start > end:         #역전 시 리턴
    return
  
  root = preorder[start]      # 루트 노드
  idx = start + 1

  while idx <= end:         # 루트보다 커지는 지점을 찾는 과정
    if preorder[idx] > root: 
      break
    idx += 1
  
  postorder(start + 1, idx - 1)     # 왼쪽 서브트리
  postorder(idx, end)           # 오른쪽 서브트리
  print(root)

preorder = []
while 1:
  try:
    preorder.append(int(input()))
  except:
    break

postorder(0, len(preorder)-1)