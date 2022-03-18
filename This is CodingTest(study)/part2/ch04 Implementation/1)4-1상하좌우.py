#5
#R R R U D D 
def RLUD():
    location = [1, 1]
    num = int(input())
    direction_list = input().split()
    for direction in direction_list:
        if direction == 'R':
            if location[1] < num:
                location[1] += 1
        elif direction == 'L':
            if location[1] > 1:
                location[1] -= 1
        elif direction == 'U':
            if location[0] > 1:
                location[0] -= 1
        else:
            if location[0] < num:
                location[0] += 1
    print(location)

RLUD()