rice_cake_count, customer_request_count = map(int, input().split())
rice_cake_list = list(map(int, input().split()))

start = 0
end = max(rice_cake_list)

result = 0
while(start <= end):
    mid = (start + end) // 2
    cutting = 0
    for rice_cake in rice_cake_list:
        if rice_cake > mid:
            cutting += (rice_cake - mid)
    if cutting < customer_request_count:
        end = (mid - 1)
    elif cutting > customer_request_count:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록한다.
        start = (mid + 1)

print(result)
