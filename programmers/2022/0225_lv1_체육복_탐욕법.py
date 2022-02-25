problem = [
    [5, [2, 4], [1, 2, 3, 5]], #5
    [5, [2, 4], [3]],       #4
    [3, [3], [1]],          #2
    [3, [1, 2, 3], [1, 2]],
    [5, [4, 2], [3, 5]]
]

def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    lost_and_reserve_student = set(lost) & set(reserve)
    if len(list(lost_and_reserve_student)) != 0:
        for student in lost_and_reserve_student:
            lost.remove(student)
            reserve.remove(student)

    taking_class_student = []
    for lost_student in lost:
        for reserve_student in reserve[:]:
            if lost_student == (reserve_student + 1) or lost_student == (reserve_student - 1):
                reserve.remove(reserve_student)
                taking_class_student.append(lost_student)
                break
    return n - (len(lost) - len(taking_class_student))

print(solution(problem[4][0], problem[4][1], problem[4][2]))