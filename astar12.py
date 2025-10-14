class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list  
        self.heuristic = heuristic  

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def h(self, node):
        """Heuristic function: estimated cost from node to goal"""
        return self.heuristic.get(node, float('inf'))

    def a_star(self, start_node, goal_node):
        open_list = set([start_node])  
        closed_list = set()  
        g = {start_node: 0}  
        parents = {start_node: None}  

        while open_list:
            current = min(open_list, key=lambda n: g[n] + self.h(n))

            if current == goal_node:
                path = []
                while current:
                    path.append(current)
                    current = parents[current]
                path.reverse()
                print("Final path:", path)
                print("Closed list (visited nodes):", closed_list)
                print("Cost g to goal:", g[goal_node])
                return path

            open_list.remove(current)
            closed_list.add(current)

            for neighbor, weight in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                tentative_g = g[current] + weight
                if neighbor not in open_list:
                    open_list.add(neighbor)
                elif tentative_g >= g.get(neighbor, float('inf')):
                    continue
                parents[neighbor] = current
                g[neighbor] = tentative_g

            print(f"Evaluated node: {current}, g={g[current]}, h={self.h(current)}, f={g[current] + self.h(current)}")

        print("No path found!")
        return None

adjacency_list = {
    'A': [('B', 2), ('C', 4),('D',1)],
    'B': [('E', 7),('F',3)],
    'C': [('F', 1)],
    'D': [('G',5)],
    'E': [('G',2)],
    'F': [('E',2)],
    'G': []
}

heuristic = {
    'A':7, 
    'B':6, 
    'C':2, 
    'D':3,
    'E':1,
    'F':1,
    'G':0
}

graph = Graph(adjacency_list, heuristic)
graph.a_star('A', 'G')
