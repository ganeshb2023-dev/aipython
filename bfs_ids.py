import math
class TreeSearchSolver:
 def __init__(self, b, d):
 self.b = b # Branching factor
 self.d = d # Goal depth
 # Total nodes up to depth d: (b^(d+1) - 1) / (b - 1)
 self.total_nodes_up_to_goal = (b**(d + 1) - 1) // (b - 1)
 self.goal_id = self.total_nodes_up_to_goal - 1
 def get_label(self, idx):

 import string
 if idx == self.goal_id:
 return "g"
 return string.ascii_uppercase[idx] if idx < 26 else
f"N{idx}"
 def solve(self):
 # (a) Nodes at depth i
 print(f"--- (a) Nodes per Depth ---")
 for i in range(self.d + 1):
 count = self.b**i
 print(f"Depth {i}: {count} nodes")
 # (b) BFS Space (Max queue size)
 bfs_space = self.b**self.d
 print(f"\n--- (b) BFS Space Requirement ---")
 print(f"Max nodes in queue: {bfs_space} (Nodes at
level d)")
 # (c) IDS Space (Max stack size)
 # DFS/IDS space is branching factor * depth limit
 ids_space = self.b * self.d
 print(f"\n--- (c) IDS Space Requirement ---")
 print(f"Max nodes in stack: {ids_space} (b * d)")
 # (d) BFS Nodes Visited
 # BFS explores level by level. Visited sequence:
 bfs_sequence = [self.get_label(i) for i in
range(self.total_nodes_up_to_goal)]
 print(f"\n--- (d) BFS Nodes Visited ---")
 print(f"Sequence: {' -> '.join(bfs_sequence)}")
 print(f"Total visited: {len(bfs_sequence)}")
 # (e) IDS Iterations
 print(f"\n--- (e) IDS Iterations ---")
 for i in range(self.d + 1):
 nodes_this_iter = (self.b**(i + 1) - 1) // (self.b - 1)
 print(f"Iteration {i} (Depth Limit {i}): Visited
{nodes_this_iter} nodes")
B_FACTOR = 2
GOAL_DEPTH = 3
solver = TreeSearchSolver(B_FACTOR, GOAL_DEPTH)
solver.solve()
