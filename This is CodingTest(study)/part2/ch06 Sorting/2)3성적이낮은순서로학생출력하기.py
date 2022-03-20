student_count = int(input())
student_and_grade_dict= {}

#각 학생과 성적을 각각 키와 값으로 만들어 student_and_grade_dict에 넣어준다.
#ex) {'홍길동': 95, '이순신': 77}
for _ in range(student_count):
    student_and_grade = input().split(' ')
    student = student_and_grade[0]
    grade = int(student_and_grade[1])
    student_and_grade_dict[student] = grade

#sorte에 key를 정해주어 정렬했다.
answer = sorted(student_and_grade_dict.items(), key = lambda item : item[1])
# for k, v in 

for i in answer:
    print(i[0], end = ' ')