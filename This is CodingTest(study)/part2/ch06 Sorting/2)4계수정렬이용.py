N, K = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1 = sorted(list1)
list2 = sorted(list2, reverse=True)

for i in range(K):
    if list1[i] < list2[i]:
        list1[i], list2[i] = list2[i], list1[i]
    else: #동빈의 원소가 크거나 같은 경우 바꿔치기를 중단한다.
        break

print(sum(list1))
