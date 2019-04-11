def sherlockAndAnagrams(s):
    substrings = get_all_substrings(s)
    count = 0
    d = {}
    for i in substrings:
        key = ''.join(sorted(i))
        if key in d.keys():
            d[key].append(i)
        else:
            d[key] = []
            d[key].append(i)
    for i in d.values():
        length = len(i)
        if length>1:
            count += ((length)*(length-1))/2
    return int(count)

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]