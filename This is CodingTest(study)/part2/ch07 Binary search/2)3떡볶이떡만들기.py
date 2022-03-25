rice_cake_count, customer_request_count = map(int, input().split())
rice_cake_list = list(map(int, input().split()))

longest = max(rice_cake_list)
for length in range(longest - 1, 0, -1):
    cut_rice_cake = 0
    for rice_cake in rice_cake_list:
        if rice_cake > length:
            cut_rice_cake += rice_cake - length
    if cut_rice_cake >= customer_request_count:
        print(length)
        break

