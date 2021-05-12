count = 0
n, m = map(int, input().split())

change_maps = [list(map(int, input())) for _ in range(n)]
result_maps = [list(map(int, input())) for _ in range(n)]

def change3x3(start_coord, arr):
    x, y = start_coord
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            change_maps[i][j] = 1 - change_maps[i][j]
            
for i in range(0, n - 2):
    for j in range(0, m - 2):
        if change_maps[i][j] != result_maps[i][j]:
            change3x3((i, j), change_maps)
            count += 1

nonResult = 0

for i in range(0, n):
    if change_maps[i] != result_maps[i]:
        nonResult = 1
        print(-1)
        break

if nonResult == 0:
    print(count)