input_file = open("pyramid_sample_input.txt","r") 
pyramid = {}
row = -1
for i in input_file.readlines():
  line = i.strip('\n').split(',')
  pyramid[row] = line
  row +=1
target = int(pyramid[-1][0].split(':')[1].strip(' '))
del pyramid[-1]
print(pyramid)

lenr = len(pyramid)
lenc = len(pyramid[lenr-1])
current2 = int(pyramid[0][0])

def dfs(row,col,val,directions):
  global lenr, target
  if row == lenr-1:
    if val*int(pyramid[row][col])==target:
      return True, directions
    else: return False,"No solution!" 
  val = val*int(pyramid[row][col])
  left = dfs(row+1,col,val,directions+'L')
  if left[0] == True: return left
  right = dfs(row+1,col+1,val,directions+'R')
  if right[0] == True: return right
  return False,"No solution!"
   
output = dfs(0,0,1,"") 
with open('pyramid_sample_output.txt', 'w') as f:
    print(output[1], file=f)