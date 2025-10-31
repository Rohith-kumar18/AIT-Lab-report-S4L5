
graph = {
    'A': {'B': 2},
    'B': {'C': 3},
    'C': {'D': 3},
    'D': {'A': 4}
}

start = 'A'
end = 'D'

path = ['A', 'B', 'C', 'D']
total_cost = 0

for i in range(len(path) - 1):
    current_node = path[i]
    next_node = path[i + 1]
    cost = graph[current_node][next_node]
    print(f"Cost from {current_node} to {next_node}: {cost}")
    total_cost += cost

print("Total Cost:", total_cost)
start = 'A'
end = 'A'

path = ['A', 'B', 'C', 'D', 'A']
total_cost = 0

for i in range(len(path) - 1):
    current_node = path[i]
    next_node = path[i + 1]
    cost = graph[current_node][next_node]
    print(f"Cost from {current_node} to {next_node}: {cost}")
    total_cost += cost

print("Total Cost:", total_cost)
