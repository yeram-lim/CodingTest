store_component_count = int(input())
store_component = list(map(int, input().split()))
customer_component_count = int(input())
customer_component = list(map(int, input().split()))

#정렬
store_component.sort()
customer_component.sort()

def binary_search(start, end, goal):
    mid = end // 2
    if goal == store_component[start] or goal == store_component[end]: #??
        return start
    elif goal == store_component[mid]:
        return mid
    elif goal > store_component[end] or goal < store_component[start]:
        return TypeError

    if goal < store_component[mid]:
        end = mid - 1
        binary_search(start, end, goal)
    elif goal > store_component[mid]:
        start = mid + 1
        binary_search(start, end, goal)


start = 0
for component in customer_component:
    store_index = binary_search(start, len(store_component) - 1, component)

    #손님이 찾는 부품이 없으면 None 반환하는 상황을 고려해 if문 작성
    if store_index is not None:
        #시작점을 반환받은 start로 지정한다. 
        #customer_component도 정렬되어 있기 때문에 이미 찾은 이전 원소(customer_component)보다 작은 store_component를 탐색할 필요가 없다.
        start = store_index
        print('yes', end=' ')
    else: 
        print('no', end=' ')
