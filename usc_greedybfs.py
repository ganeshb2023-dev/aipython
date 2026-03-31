import heapq
graph={
 'a':[('b',32),('f',3)],
 'b':[('a',32),('e',12),('f',7),('c',21)],
 'f':[('a',3),('b',7),('c',2)],
 'e':[('b',12),('c',6),('d',13)],
 'c':[('f',2),('b',21),('e',6),('g',11)],
 'd':[('e',13),('g',9)],
 'g':[('c',11),('d',9)]
 }
def uniform_cost_search(graph,start,goal):
 pq=[(0,start,[])]
 visited=set()
 while pq:
 cost,node,path=heapq.heappop(pq)
 if node in visited:
 continue
 path=path+[node]
 visited.add(node)
 if node==goal:
 return cost,path
 for neighbor,weight in graph[node]:
 if neighbor not in visited:
 heapq.heappush(pq,(cost+weight,neighbor,path))
 return None
heuristic={
 'a':8,
 'b':5,
 'c':8,
 'd':5,
 'e':3,
 'f':7,
 'g':0}
def greedy_bfs(graph,start,goal,heuristic):
 pq=[(heuristic[start],start,[])]
 visited=set()
 while pq:
 h,node,path=heapq.heappop(pq)
 if node in visited:
 continue
 path=path+[node]
 visited.add(node)
 if node==goal:
 return path
 for neighbor,_ in graph[node]:
 if neighbor not in visited:
 heapq.heappush(pq,(heuristic[neighbor],neighbor,path))
 return None
start_node='a'
goal_node='g'
ucs_result=uniform_cost_search(graph,start_node,goal_node)
result=greedy_bfs(graph,start_node,goal_node,heuristic)
print("Greedy BFS:",result)
print("Uniform cost search:")
print("cost:",ucs_result[0])
print("path:",ucs_result[1])
