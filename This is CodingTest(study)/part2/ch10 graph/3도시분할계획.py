house_count, path_count = map(int, input().split())
parent = [0] * (house_count + 1)
edges = []
result = 0
higest_cost = 0

for i in range(1, house_count + 1):
    parent[i] = i

for _ in range(path_count):
    house1, house2, cost = map(int, input().split())
    edges.append((cost, house1, house2))

edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    if find_parent(parent, a) < find_parent(parent, b):
        parent[b] = a
    else:
        parent[a] = b


for edge in edges:
    cost, house1, house2 = edge
    if find_parent(parent, house1) != find_parent(parent, house2): #같은 집합 x
        union_parent(parent, house1, house2)
        result += cost
        if higest_cost < cost:
            higest_cost = cost

print(result - higest_cost)
print(result, higest_cost)