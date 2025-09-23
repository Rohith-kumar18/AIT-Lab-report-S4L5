graph = {'A': {'B':2, 'C':3},
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F': [],
     'G': []}


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            paths += find_all_paths(graph, node, end, path)

    return paths

print("Path : ",find_all_paths(graph, 'A', 'F'))

cost= cost + (str(graph['A'].get('B')+(graph['A'].get('C'))))
