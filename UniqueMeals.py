import collections
def unique(meals):
  if not meals:
    return None
  d = collections.defaultdict(list)
  for i in meals:
    d[tuple(sorted(i["dish"]))].append(i["cuisine"])
  print(d)

eg = [{"cuisine":"x","dish":["a","b","c"]},{"cuisine":"y","dish":["b","c","d"]},{"cuisine":"z","dish":["b","a","c"]}]
unique(eg)