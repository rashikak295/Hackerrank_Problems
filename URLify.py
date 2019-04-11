def URLify(s, l):
  space = 0
  index = 0
  s = s.rstrip()#get rid of trailing spaces
  for i in s:
    if i == ' ':
      space+= 1 #count spaces
  index = l + space*2
  s = s + ' '*(space*2)
  s = list(s)
  for i in range(l-1, -1, -1):
    if s[i] == ' ':
      s[index-1]='0'
      s[index-2]='2'
      s[index-3]='%'
      index = index - 3
    else:
      s[index-1]=s[i]
      index = index - 1
  s = ''.join(s)#convert string to list
  return s

print(URLify("Mr John Smith   ", 13))