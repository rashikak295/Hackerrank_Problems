def countTriplets(arr, r):
    pairs = collections.defaultdict(int)
    count = collections.defaultdict(int)
    total = 0
    for i in arr[::-1]:
        if i*r in pairs: total += pairs[i*r]
        if i*r in count: pairs[i] += count[i*r]
        count[i] +=1
    return total