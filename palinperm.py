def palinperm(s):
  count = 0
  s = s.replace(" ", "")
  s = s.lower()
  c = {chr(i):0 for i in range(129)}
  for i in s:
    c[i]+= 1
  for i in c:
    if c[i]%2 != 0:
      count+= 1
      if count>1:
        return False
  return True

print(palinperm("Tact Coa"))