class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 1
        l = len(s)
        cur = 1
        all_cur = []
        if l == 0: return 0
        elif l == 1: return 1
        else:
            while 1<=j<l and 0<=i<l:
                if s[j] not in s[i:j]:
                    cur += 1
                    j += 1
                else:
                    while s[i] != s[j]:
                        i += 1
                    i += 1
                    all_cur.append(cur)
                    cur = j-i
            all_cur.append(cur)
            return max(all_cur)         