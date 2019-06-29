def path(r,c):
  memo = [[0 for i in range(r)] for j in range(c)]
  return path2(r-1,c-1,memo)

def path2(r,c,memo):
  if r==0 or c==0:
    return 1
  if memo[r][c] ==0:
    if r-1>=0:
      memo[r][c] += path2(r-1,c,memo)
    if c-1>=0:
      memo[r][c] += path2(r,c-1,memo)
  return memo[r][c]

print(path(5,5))


# Grid with obstacles
# def path(grid):
#   r = len(grid)
#   c = len(grid[0])
#   memo = grid
#   return path2(r-1,c-1,memo)

# def path2(r,c,memo):
#   if (r==0 or c==0) and memo[r][c] != -1:
#     return 1
#   if memo[r][c] == -1:
#     return 0
#   if memo[r][c] ==0:
#     if r-1>=0:
#       memo[r][c] += path2(r-1,c,memo)
#     if c-1>=0:
#       memo[r][c] += path2(r,c-1,memo)
#   return memo[r][c]

# grid = [[0,0,0,0],[0,-1,-1,0],[0,0,0,0],[0,-1,0,0]]
# print(path(grid))


def path(grid):
  r = len(grid)
  c = len(grid[0])
  memo = grid
  return path2(0,0,r-1,c-1,memo,"")

def path2(ridx,cidx,r,c,memo,direc):
  if (ridx == r-1 and cidx == c): 
    if memo[ridx][cidx]!=-1:
      direc = direc+'D'
      return True, direc
    else: return False, "No solution!"
  if (ridx == r and cidx == c-1):
    if memo[ridx][cidx]!=-1: 
      direc = direc+'R'
      return True, direc
    else: return False, "No solution!"
  if ridx>r or cidx>c: return False, "No solution!"
  if memo[ridx][cidx]==-1 : return False, "No solution!"
  right = path2(ridx,cidx+1,r,c,memo,direc+'R')
  if right[0]== True: return right
  down = path2(ridx+1,cidx,r,c,memo,direc+'D')
  if down[0]== True: return down
  memo[ridx][cidx] = -1
  return False,"No solution!" 

grid = [[0,-1,0,-1],[-1,-1,-0,0],[0,0,0,0],[0,-1,0,0]]
print(path(grid)[1])

