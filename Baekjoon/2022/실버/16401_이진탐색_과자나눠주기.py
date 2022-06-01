from sys import stdin
input = stdin.readline

children_count, snack_count = map(int, input().split())
snacks = list(map(int, input().split()))

snacks.sort(reverse=True)
result = 0

start = 0
end = max(snacks)

while start <= end:
    total = 0
    mid = (start + end) // 2

    if mid == 0:
        break

    # print('start is ', start, 'end is ', end )
    # print('-----')
    for snack in snacks:
        if snack >= mid:
            total += (snack // mid)
            # print('snack is ', snack, 'total is ', total)
        else:
            # print('snack is ', snack, 'total is ', total)
            break

    if total >= children_count:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
# print(children_count, snack_count, snacks)