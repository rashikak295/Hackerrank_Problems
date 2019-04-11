def freqQuery(queries):
    array = collections.defaultdict(int)
    freq = collections.defaultdict(list)
    ans = []
    for i in queries:
        if i[0] == 1:
            if i[1] in array.keys(): freq[array[i[1]]].remove(i[1])
            array[i[1]] +=1
            freq[array[i[1]]].append(i[1])
        if i[0] == 2:
            if i[1] in array.keys():
                freq[array[i[1]]].remove(i[1])
                array[i[1]] -=1
                if array[i[1]]<1: del array[i[1]]
                else: freq[array[i[1]]].append(i[1])
        elif i[0] == 3:
            if len(freq[i[1]])>0: ans.append(1)
            else: ans.append(0)
    return ans