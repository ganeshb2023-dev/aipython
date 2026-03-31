from collections import deque
def bfs(graph, start):
 visited = set()
 queue = deque()
 visited.add(start)
 queue.append(start)
 print("BFS traversal:", end=" ")
 # print(queue)
 # print(visited)

 while queue:
 node = queue.popleft()
 print(node, end=" ")
 for neigh in graph[node]:
 if neigh not in visited:
 visited.add(neigh)
 queue.append(neigh)
 print()
# number of vertices
n = int(input("Enter number of vertices: "))
# read all vertex labels (could be numbers or strings)
print("Enter vertex labels separated by space:")
vertices = input().split()
# build empty adjacency list
graph = {v: [] for v in vertices}
# number of edges
m = int(input("Enter number of edges: "))
print("Enter each edge as: u v ")
for _ in range(m):
 u, v = input().split()
 # assuming undirected graph; for directed,
 #remove one of the two lines
 graph[u].append(v)
 graph[v].append(u)
# choose start vertex
start = input("Enter start vertex for BFS: ")
# run BFS
if start not in graph:
 print("Start vertex not in graph!")
else:
 bfs(graph, start)
