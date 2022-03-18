#5, 11475
def findThreeInTime():
    hour = input()
    threeIn60 = 0
    for i in range(59):
        if "3" in str(i + 1):
            threeIn60 += 1

    answer = 0
    for i in range(int(hour)+1):
        if (i % 3) == 0:
            answer += (60 ** 2)
        else:
            answer += (threeIn60 ** 2 + threeIn60)
        print(answer)

    print(answer)
findThreeInTime()

def book():
    h = int(input())

    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)