conference_count = int(input())
schedule = []
for conference in range(conference_count):
    schedule.append(tuple(map(int, input().split())))
schedule.sort(key=lambda tup: tup[0])

result = [[schedule[0]]]
for schedule_time in schedule[1:]:
    put = 0
    for idx, result_time in enumerate(result[:]):
        # print("result is ", result)
        # print("result time is ", idx, result_time)
        if result_time[-1][1] <= schedule_time[0]: #맨 마지막 회의 끝나는 시간 > 예정회의 시작시간
            result_time.append(schedule_time)
            put += 1
        elif idx == len(result) - 1 and put == 0:
            result.append([schedule_time])
# [
#     [(0, 6), (6, 10), (12, 14)], 
#     [(1, 4), (5, 7), (8, 11), (12, 14)], 
#     [(2, 13)], 
#     [(3, 5), (5, 7), (8, 11), (12, 14)], 
#     [(3, 8), (8, 11), (12, 14)], 
#     [(5, 9), (12, 14)], 
#     [(8, 12), (12, 14)]
# ]

answer = max(result, key=lambda time: len(time))
print(len(answer))

print(schedule)
print(result)