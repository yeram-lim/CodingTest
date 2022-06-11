import re

count = int(input())

answer = []

for i in range(count):
    homework = input()
    try:
        int_homework = int(homework)
        answer.append(int_homework)
    except ValueError:
        numbers = re.findall(r'\d+', homework)

        for num in numbers:
            answer.append(int(num))

for i in sorted(answer):
    print(i)