graph = {
    "A": ["B", "D"],
    "B": ["C", "F"],
    "C": ["E", "G"],
    "D": ["F"],
    "E": ["B", "F"],
    "F": ["A"],
    "G": ["E"]
}


# visited = set()
#
#
# def DFS(visited, graph, node):
#     if node not in visited:
#         print(node, end=" ")
#
#         visited.add(node)
#         for neighbour in graph[node]:
#             DFS(visited, graph, neighbour)
#

def dfs(adjacencyList, startNode):
    stack = [startNode]
    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in reversed(adjacencyList[node]):
                if neighbour not in visited:
                    stack.append(neighbour)


# DFS(visited, graph, "A")
dfs(graph, "A")
