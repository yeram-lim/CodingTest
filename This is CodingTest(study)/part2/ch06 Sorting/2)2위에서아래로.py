data_count = int(input())
data_list = []
for _ in range(data_count):
    data_list.append(int(input()))

data_list = sorted(data_list, reverse=True)

for data in data_list:
    print(data, end = ' ')
