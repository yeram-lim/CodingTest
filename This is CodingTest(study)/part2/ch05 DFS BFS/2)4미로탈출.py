# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]
print(bfs(0,0))