computer_count = int(input())
network_count = int(input())

graph = [[] for _ in range(computer_count + 1)]
for i in range(network_count):
    from_com, to_com = map(int, input().split())
    graph[from_com].append(to_com)
    graph[to_com].append(from_com)
#graph = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

strat_com = 1
get_attacked_com = []

for com_num in range(1, computer_count + 1):
    for linked_com in graph[com_num]: #[2,5]
        if linked_com is 0: #만약 0이면 아래에서 오류냠
            continue #forloop 하나만 건너뜀, pass는 계속 진행, break은 for문 자체를 뛰어넘음
        attecked_index = graph[com_num].index(linked_com)
        parent_index = graph[linked_com].index(com_num) #graph[0]에 아무것도 없어서 오류 남
        if linked_com not in get_attacked_com:
            get_attacked_com.append(linked_com)
            graph[com_num][attecked_index] = 0
            graph[linked_com][parent_index] = 0
            print('this com is ', com_num, 'linked com is ',linked_com,)
            print(linked_com, 'is not attacked')
            print('the graph is ',graph, 'attacked is ', get_attacked_com)
            print('-----')
        else:
            graph[com_num][attecked_index] = 0
            graph[linked_com][parent_index] = 0
            print('this com is ', com_num, 'linked com is ',linked_com,)
            print(linked_com, 'is attacked')
            print('the graph is ',graph, 'attacked is ', get_attacked_com)
            print('-----')

print(graph, get_attacked_com)