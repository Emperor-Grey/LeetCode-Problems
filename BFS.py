from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": ["A"]
}


def BFS(adjacencyList, startNode):
    visited = [startNode]
    queue = deque([startNode])

    while queue:
        first_node = queue.popleft()
        print(first_node, end=" ")

        for neighbour in adjacencyList[first_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


BFS(graph, "A")
