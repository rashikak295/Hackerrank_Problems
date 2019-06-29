l = ([1,2,3],[4,5,6],[7,8,9])
t = 11
flag = 1
i,j = 0,len(l[0])-1
while l[i][j] != t :
  if l[i][j] > t:
    j -= 1
    if j<0 or j>len(l[0])-1:
      flag = 0
      break
  elif l[i][j] < t:
    i += 1
    if i<0 or i>len(l)-1:
      flag = 0
      break

if flag == 1:
  print(i,j) 
else: print("No Solution!")