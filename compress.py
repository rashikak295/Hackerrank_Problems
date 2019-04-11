#def compress(s):
#  s2 = []
#  count=1
#  for i in range(len(s)):
#    if i == 0 or s[i]!=s[i-1]:
#      if i != 0:
#        s2.append(str(count))
#      count = 1
#      s2.append(s[i])
#    else:
#     count+= 1
#      if i == len(s)-1:
#        s2.append(str(count))
#  if len(s2) >= len(s):
#    return s
#  s2 = ''.join(s2)
#  return s2
#print(compress("aabbcc"))

def compress(s):
  s2 = []
  count=0
  for i in range(len(s)):
    count+=1
    if i+1>= len(s) or s[i]!=s[i+1]:
      s2.append(s[i])
      s2.append(str(count))
      count=0
  if len(s2) >= len(s):
    return s
  s2 = ''.join(s2)
  return s2
print(compress("aabccc"))