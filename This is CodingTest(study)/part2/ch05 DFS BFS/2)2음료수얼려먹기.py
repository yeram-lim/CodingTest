# 4 5
# 00110
# 00011
# 11111
# 00000


n, m = map(int, input().split())

graph = []
# [[0, 0, 1, 1, 0], 
#   [0, 0, 0, 1, 1], 
#   [1, 1, 1, 1, 1], 
#   [0, 0, 0, 0, 0]]

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    print(graph)
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)