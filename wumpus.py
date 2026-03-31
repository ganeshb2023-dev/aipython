SIZE=4
start=(1,1)
pit=(1,3)
wumpus=(3,3)
gold=(4,4)
moves=[(1,0),(-1,0),(0,1),(0,-1)]
def adjacent(cell):
 x,y=cell
 cells=[]
 for dx,dy in moves:
 nx=x+dx
 ny=y+dy
 if 1<=nx <= SIZE and 1<=ny <=SIZE:
 cells.append((nx,ny))
 return cells
def percept(cell):
 p=[]
 if cell in adjacent(pit):
 p.append("Breeze")
 if cell in adjacent(wumpus):
 p.append("stench")
 if cell==gold:
 p.append("Glitter (Gold)")

 return p
def print_grid(agent):
 print("\nWumpus world\n")
 for i in range(SIZE,0,-1):
 for j in range(1,SIZE+1):
 cell =(i,j)
 if cell ==agent:
 print("A",end="")
 elif cell ==pit:
 print("P",end="")
 elif cell==wumpus:
 print("W",end="")
 else:
 print(".",end="")
 print()
 print()
def explore():
 visited =set()
 safe={(1,1)}
 stack=[(1,1)]
 step =1
 while stack:
 current =stack.pop()
 if current in visited:
 continue
 visited.add(current)
 print("STEP",step)
 print_grid(current)
 print("Agent position:",current)
 if current==pit:
 print("Agent fell into PIT")
 return
 if current==wumpus:
 print("Wumpus killed the agent")
 return
 p=percept(current)
 if p:
 print("percept:",p)
 else:
 print("percept: None")
 if current==gold:
 print("Gold found")
 return
 if "Breeze" not in p and "Stench" not in p:
 for n in adjacent(current):
 if n not in visited:
 safe.add(n)
 stack.append(n)
 step+=1
explore()
