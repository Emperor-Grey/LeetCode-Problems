from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": ["A"]
}


def bfs(adjacency_list, start_node):
    visited = [start_node]
    queue = deque([start_node])

    while queue:
        first_node = queue.popleft()
        print(first_node, end=" ")

        for neighbour in adjacency_list[first_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(graph, "A")
