import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

def preorder(in_l, in_r, post_l, post_r):
  if in_l > in_r or post_l > post_r:
    return
  root = postorder[post_r]
  print(root, end=" ")

  left = idx[root] - in_l
  right = in_r - idx[root]

  preorder(in_l, in_l+left-1, post_l, post_l+left-1)
  preorder(in_r-right+1, in_r, post_r-right, post_r-1)

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx = [0] * (n+1)

for i in range(n):
  idx[inorder[i]] = i

preorder(0, n-1, 0, n-1)
