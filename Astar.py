import heapq
# Capacities of the jugs
JUG_A = 4 # 4-gallon jug
JUG_B = 3 # 3-gallon jug
# Goal amount in 4-gallon jug
GOAL = 2
def heuristic(state):
 """Heuristic: distance from goal in 4-gallon jug"""
 a, b = state
 return abs(a - GOAL)
def get_successors(state):
 """Generate all valid successor states"""
 a, b = state
 successors = []
 # Fill jug A
 successors.append((JUG_A, b))
# Fill jug B
 successors.append((a, JUG_B))
 # Empty jug A
 successors.append((0, b))
 # Empty jug B
 successors.append((a, 0))
 # Pour A -> B
 pour = min(a, JUG_B - b)
 successors.append((a - pour, b + pour))
# Pour B -> A
 pour = min(b, JUG_A - a)
 successors.append((a + pour, b - pour))
 return successors
def a_star():
 start = (0, 0)
# Priority queue stores (f, g, state, path)
 pq = []
 heapq.heappush(pq, (heuristic(start), 0, start, [start]))
 visited = set()
 while pq:
 f, g, current, path = heapq.heappop(pq)
 if current in visited:
 continue
 visited.add(current)
if current[0] == GOAL:
 return path
 for nxt in get_successors(current):
 if nxt not in visited:
 g_new = g + 1
 f_new = g_new + heuristic(nxt)
 heapq.heappush(pq, (f_new, g_new, nxt, path + [nxt]))
 return None
# Run A* search
solution = a_star()
print("Solution Path:")
for step in solution:
 print(step)
