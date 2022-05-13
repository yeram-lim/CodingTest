
def firstStep(list, num, x, y, counting):
    for i in range(counting):
        list[x][y] = num
        x += 1
        num += 1
    return (num, x - 1, y + 1)

def secondStep(list, num, x, y, counting):
    for i in range(counting):
        list[x][y] = num
        y += 1
        num += 1
    return (num, x - 1, y- 2)

def thirdStep(list, num, x, y, counting):
    for i in range(counting):
        list[x][y] = num
        x -= 1
        y -= 1
        num += 1
    return (num, x + 2, y + 1)

def solution(n):
    triangle = []
    for i in range(1, n + 1):
        triangle.append([0] * i)

    x, y = 0, 0
    num = 1
    counting = len(triangle) #한 줄 돌아가면서 연산(숫자 바꿀)의 수
    step = 1

    while counting:
        if step == 1:
            num, x, y = firstStep(triangle, num, x, y, counting)
            counting -= 1
            step = 2
            print('after first ', x, y, counting)
        elif step == 2:
            num, x, y = secondStep(triangle, num, x, y, counting)
            counting -= 1
            step = 3
            print('after second ', x, y, counting)
        else:
            num, x, y = thirdStep(triangle, num, x, y, counting)
            counting -= 1
            step = 1
            print('after third ', x, y, counting)

    answer = []
    for i in triangle:
        answer.extend(i)

    return answer

solution(6)