def isValid(s):
    sdict = collections.Counter(s)
    common = collections.Counter(sdict.values()).most_common(1)[0][0]
    flag = 1
    for i in sdict.values():
        if abs(common-i)>1 and i!=1:
            return "NO"
        elif abs(common-i)==1 and flag==1:
            flag=0
        elif abs(common-i)==1 and flag==0:
            return "NO"
    return "YES"