from collections import deque
V = 3
E = 2
adj = {{1,2,3}, {}, {4}, {}, {}}
def Graph(V, adj):
    visited = [False] * V
    queue = deque([0])
    result = []

    while queue:
        node = queue.popleft()
        if not visited[node]:
            result.append(node)
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
    return result
print(Graph(V, adj))