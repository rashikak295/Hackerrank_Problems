def makeAnagram(a, b):
    adict = collections.Counter(a)
    bdict = collections.Counter(b)
    count = 0
    for i in adict.keys():
        if i not in bdict.keys(): count += adict[i] 
        elif adict[i]>bdict[i]: count += adict[i] - bdict[i]
    for i in bdict.keys():
        if i not in bdict.keys(): count +=bdict[i]
        elif bdict[i]>adict[i]: count +=bdict[i] - adict[i]
    return count