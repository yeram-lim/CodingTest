conference_count = int(input())
schedule = []
for conference in range(conference_count):
    schedule.append(tuple(map(int, input().split())))
schedule.sort(key=lambda tup: (tup[1], tup[0]))
#[(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

count = 1
end = schedule[0][1]
for schedule_time in schedule[1:]:
    if schedule_time[0] >= end:
        end = schedule_time[1]
        count += 1

print(count)
