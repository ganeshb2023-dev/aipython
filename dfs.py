from collections import defaultdict
def dfs_traversal(graph, start, visited=None):
 """
 Performs DFS traversal even if graph has cycles.
 Prints the order of visitation.
 """
 if visited is None:
 visited = set()

 visited.add(start)
 print(start, end=" ")

 for neighbour in graph[start]:
 if neighbour not in visited:
 dfs_traversal(graph, neighbour, visited)
# User input (same format as your previous codes)
n = int(input("Enter number of vertices:"))
print("Enter vertex labels separated by space:")
vertices = input().split()
m = int(input("Enter number of edges:"))
# Build graph using defaultdict
graph = defaultdict(list)
for _ in range(m):
 print("Enter edge (u v):")
 u, v = input().split()
 graph[u].append(v)
 graph[v].append(u) # Undirected graph
print("Enter start vertex for DFS:")
start = input().strip()
print("DFS Traversal:", end=" ")
if start not in graph:
 print(f"Start vertex '{start}' not in graph!")
else:
 dfs_traversal(graph, start)
 print() # New li
