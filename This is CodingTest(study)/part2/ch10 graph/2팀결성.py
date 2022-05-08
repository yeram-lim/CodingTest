team_count, calculation = map(int, input().split())
parent = [0] * (team_count + 1) #[0, 0, 0, 0, 0, 0, 0, 0]

#각 num번 팀에 num번 학생을 속하게 한다.
for num in range(team_count + 1): #[0, 1, 2, 3, 4, 5, 6, 7]
    parent[num] = num

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, student1, student2):
    student1 = find_parent(parent, student1)
    student2 = find_parent(parent, student2)
    if student1 < student2:
        parent[student2] = student1
    else:
        parent[student1] = student2

print()

for _ in range(calculation):
    cal, student1, student2 = map(int, input().split())
    if cal:
        student1 = find_parent(parent, student1)
        student2 = find_parent(parent, student2)
        if student1 == student2:
            print('YES', end = " ")
        else:
            print('NO', end = " ")
    else:
        union_parent(parent, student1, student2)