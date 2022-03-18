# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

from re import T
from winreg import DisableReflectionKey


def gameCharcter():
    height, width = map(int, input().split())
    x, y, direction = input().split()
    game_map = []
    for i in range(height):
        game_map.append(input().split())
    print(game_map)

# gameCharcter()

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def book():
    n, m = map(int, input().split())

    d = [[0] * m for _ in range(n)] #4*4 육지를 만듦
    x, y, direction = map(int, input().split())
    d[x][y] = 1 #캐릭터의 좌표를 방문 처리

    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
    
    #북 동 남 서 방향 정의
    dx = [-1, 0, 1, 0] 
    dy = [0, 1, 0, -1] 

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
book()