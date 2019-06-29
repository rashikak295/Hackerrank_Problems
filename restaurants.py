import collections

restaurants = {"American":"[burgur, potato chips]","Italian":"[pizza, potato chips]"}

out = collections.defaultdict(list)
out2 = collections.defaultdict(int)

for i in restaurants.keys():
  restaurants[i] = restaurants[i][1:-1].split(",")
  for j in restaurants[i]:
    out[j.strip(" ")].append(i)
for k in out.keys():
  out2[k] = len(out[k])

print(out2)