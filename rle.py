class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        write = 0
        for c in range(len(chars)):
            if c+1 != len(chars) and chars[c+1] == chars[c]:
                count += 1
            elif c+1 == len(chars) or chars[c+1] != chars[c]:
                if count == 1:
                    chars[write]= chars[c]
                    write += 1
                else: 
                    l = len(chars[c]+str(count))
                    chars[write:write+l] = chars[c]+str(count)
                    write = write+l
                count = 1
        return write     