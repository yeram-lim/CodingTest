count = int(input())
candy_list = [list(input()) for _ in range(count)]
answer = 0

def check(candy_list):
    answer = 1 

    for i in range(count): #0 1 2
        cnt = 1
        #열고정
        for idx in range(1, count): #1 2
            if candy_list[i][idx] == candy_list[i][idx - 1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > answer:
                answer = cnt

        cnt = 1
        #행고정
        for idx in range(1, count):
            if candy_list[idx][i] == candy_list[idx - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt
    return answer

for row in range(count):
    for col in range(count):
        if col + 1 < count:
            candy_list[row][col], candy_list[row][col + 1] = candy_list[row][col + 1], candy_list[row][col]
            temp = check(candy_list)

            if temp > answer:
                answer = temp

            candy_list[row][col], candy_list[row][col + 1] = candy_list[row][col + 1], candy_list[row][col]


        if row + 1 < count:
            candy_list[row][col], candy_list[row + 1][col] = candy_list[row + 1][col], candy_list[row][col]
            temp = check(candy_list)

            if temp > answer:
                answer = temp

            candy_list[row][col], candy_list[row + 1][col] = candy_list[row + 1][col], candy_list[row][col]
            
print(answer)
