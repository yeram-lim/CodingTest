storage_count = int(input())
storage = list(map(int, input().split()))

d = [0] * 100
d[0] = storage[0]
d[1] = max(storage[0], storage[1])

for i in range(2, storage_count):
    d[i] = max(d[i -1], d[i - 2] + storage[i])

print(d[storage_count -1])