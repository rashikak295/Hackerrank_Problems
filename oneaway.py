def oneaway(s1,s2):
  count = 0
  if len(s1) == len(s2):
    for i in range(len(s1)):
      if s1[i] != s2[i]: count+= 1
      if count>1: return False
    return True
  elif abs(len(s1)-len(s2)) == 1:
    p1=0
    p2=0
    if len(s2)>len(s1): 
      s=s2
      s2=s1
      s1=s
    while(p1!=len(s1) and p2!=len(s2)):
      if s1[p1] != s2[p2]:
        count+= 1
        if count>1: return False
      else: p2+=1
      p1+=1
    return True
  else:
    return False

print(oneaway("ple","pale"))