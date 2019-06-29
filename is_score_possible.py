def is_total(arr, n):
  if n in arr:
    return True
  for i in arr:
    if i<=n:
      F = is_total(arr,n-i)
      if F: return F
  return False
print(is_total({2,3,6},7))