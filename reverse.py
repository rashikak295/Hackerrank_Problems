def reverse(s1,s2):
  if len(s1)!=len(s2):
    return False
  if s1 == "" and s2 == "":
    return True
  else:
    length = len(s1)
    for i in range(length):
      if s1[i] != s2[length - i -1]:
        return False
    return True


print(reverse("asd","dsa"))