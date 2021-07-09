import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
INF = sys.maxsize

def dfs(cur, p):
	par[cur] = p
	size[cur] = 1
	for nxt in graph[cur]:
		if nxt != p:
			size[cur] += dfs(nxt, cur)
	return size[cur]

def HLD(cur, p, cur_chain, d):

	depth[cur] = d
	chain_num[cur] = cur_chain
	chain_idx[cur] = len(chain[cur_chain])
	chain[cur_chain].append(cur)

	heavy = -1

	for nxt in graph[cur]:
		if nxt != p and (heavy == -1 or size[nxt] > size[heavy]):
			heavy = nxt
	if heavy != -1:
		HLD(heavy, cur, cur_chain, d)
	for nxt in graph[cur]:
		if nxt != p and nxt != heavy:
			HLD(nxt, cur, nxt, d + 1)


def LCA(a, b):
	while chain_num[a] != chain_num[b]:
		if depth[a] > depth[b]:
			a = par[chain_num[a]]
		else:
			b = par[chain_num[b]]
	return b if chain_idx[a] > chain_idx[b] else a

n = int(input())
N = n + 1

graph = [[] for _ in range(N)]

depth = [0] * N
chain_num = [0] * N
chain_idx = [0] * N
chain = [[] for _ in range(N)]
size = [0] * N
par = [0] * N

for _ in range(n - 1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

dfs(1, 0)
HLD(1, 0, 1, 0)

M = int(input())
for _ in range(M):
	a, b = map(int, input().split())
	print(LCA(a, b))