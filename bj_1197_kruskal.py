import sys
input = sys.stdin.readline

V, E = map(int, input().split())

vRoot = list(range(V + 1))
edges = [list(map(int, input().split())) for _ in range(E)]

edges.sort(key=lambda x:x[2])

def find(x):
    if x != vRoot[x]:
        vRoot[x] = find(vRoot[x])
    return vRoot[x]

ans = 0
cnt = 0

for u, v, w in edges:
    if cnt == V-1:
        break

    ru, rv = find(u), find(v)
    
    if ru != rv:
        vRoot[ru] = vRoot[rv] = min(ru, rv)
        ans += w
        cnt += 1

print(ans)
