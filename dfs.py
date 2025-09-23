graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

dfs(graph, '5')
