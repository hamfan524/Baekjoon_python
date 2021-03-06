import sys
from collections import deque

input = sys.stdin.readline
def add(trie, text):
  cur = trie
  for i in text:
    if i not in cur:
      cur[i] = {}
    cur = cur[i]
  cur['*'] = {}

def bfs(trie):
  q = deque([trie])
  while q:
    cur = q.popleft()
    if len(cur) >= 2 and '*' in cur:
      return False
    else:
      for i in cur:
        q.append(cur[i])
  return True

def solution(n, text):
  trie = {}
  for i in range(n):
    add(trie, text[i])
  if bfs(trie):
    print("YES")
  else:
    print("NO")

t = int(input())
for _ in range(t):
  n = int(input())
  text = []
  for _ in range(n):
    text.append(input().rstrip())
  solution(n, text)