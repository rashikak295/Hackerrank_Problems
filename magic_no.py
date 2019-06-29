def magic_no(array,l,r):
  if r>=l:
    mid = l+ (r-l)//2
    if mid==array[mid]:
      return mid
    if mid<array[mid]:
      return magic_no(array,l,mid-1)
    if mid>array[mid]:
      return magic_no(array,mid+1,r)
  return None

print(magic_no([-1,0,1,3,5],0,4))

# def magic_no(array,l,r):
#   if r>=l:
#     mid = l+ (r-l)//2
#     if mid==array[mid]:
#       return mid
#     lidx = min(array[mid],mid-1)
#     left = magic_no(array,l,lidx)
#     if left!=None: return left
#     ridx = max(array[mid],mid+1)
#     right = magic_no(array,ridx,r)
#     return right
#   return None

# print(magic_no([-10,-5,2,2,2,3,4,7,9,12,13],0,10))