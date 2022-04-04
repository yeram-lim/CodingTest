num = int(input())

d = [0] * num
answer = 0
def calculation(num):
    if num % 5 == 0:
        # d[5]
        answer += 1
#큰수에서 나눠야해서 탑다운인줄 알았다. 그래서 재귀를 해보려고 했다.

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    print('before ', d[i])
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

print('after', d[i])
print('------')

# print
    
