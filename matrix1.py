
graph=[
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
print("Elements of graph:")
for i in graph:
    print(i)
start=(0,0)
end=(2,1)
    
graph = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

start = (0,0)
end = (2,1)
def is_valid(x, y, visited):
    rows, cols = len(graph), len(graph[0])
    return (0 <= x < rows and 0 <= y < cols and
            graph[x][y] == 0 and (x, y) not in visited)

def find_all_paths(current, end, path, visited, all_paths):
    if current == end:
        all_paths.append(path[:])  
        return
    
    x, y = current
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited):
            visited.add((nx, ny))
            path.append((nx, ny))
            find_all_paths((nx, ny), end, path, visited, all_paths)
            path.pop()
            visited.remove((nx, ny))

all_paths = []
visited = {start}
find_all_paths(start, end, [start], visited, all_paths)

print(f"All paths from {start} to {end} avoiding '1':")
for i, p in enumerate(all_paths, 1):
    print(f"Path {i}: {p}")
