def ok(mL, cL, M, C):
 mR, cR = M - mL, C - cL
 if min(mL, cL, mR, cR) < 0:
 return False
 if mL > 0 and cL > mL:
 return False
 if mR > 0 and cR > mR:
 return False
 return True
def nbrs(s, M, C, K):
 mL, cL, b = s
 for m in range(K + 1):
 for c in range(K + 1):
 if m + c == 0 or m + c > K:
 continue
 sign = -1 if b == 0 else 1
 nmL, ncL = mL + sign * m, cL + sign * c
 nb = 1 - b
 if ok(nmL, ncL, M, C):
 yield (nmL, ncL, nb)
def bfs(M, C, K):
 start, goal = (M, C, 0), (0, 0, 1)
 q = deque([start])
 parent = {start: None}
 while q:
 cur = q.popleft()
 if cur == goal:
 path = []
 while cur is not None:
 path.append(cur)
 #print(path)
 cur = parent[cur]
 return path[::-1]
 for nxt in nbrs(cur, M, C, K):
 if nxt not in parent:
 parent[nxt] = cur
 q.append(nxt)
return None
M = int(input("Missionaries: "))
C = int(input("Cannibals: "))
K = int(input("Boat capacity: "))
sol = bfs(M, C, K)
if sol:
 print("State: (M_left, C_left, boat_side) ; 0=left, 1=right")
 for i, s in enumerate(sol):
 print(f"Step {i}: {s}")
else:
 print("No solution.")
