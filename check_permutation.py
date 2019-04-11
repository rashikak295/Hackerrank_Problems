def permutation(s,t):
  if (len(s)!=len(t)):
    return False
  letters = {chr(i):0 for i in range(129)}
  for i in range(len(s)):
    letters[s[i]]+=1
  for j in range(len(t)):
    letters[t[j]]-=1
    if(letters[t[j]]<0):
      return False
  return True

print(permutation("asfs","asfg"))