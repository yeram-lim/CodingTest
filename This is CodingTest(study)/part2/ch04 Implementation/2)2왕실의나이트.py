#a1

import enum


def getLocationOfNight():
    current_location = input()
    direction_list = ['vertical', 'horizontal']
    movement_list = [1, 2]

    count = 0
    for direction_idx, direction in enumerate(direction_list):
        for movement in movement_list:
            if direction == 'vertical':
                pass

def getLocationOfNight2():
    input_data = input()
    current_location = [int(ord(input_data[0])) - int(ord('a')) + 1, int(input_data[1])]

    movement_list = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    count = 0
    for movement in movement_list:
        location_x = current_location[0] + movement[0]
        location_y = current_location[1] + movement[1]
        if location_x < 1 or location_x > 8:
            pass
        elif location_y < 1 or location_y > 8:
            pass
        else:
            count += 1

    print(count)
getLocationOfNight2()