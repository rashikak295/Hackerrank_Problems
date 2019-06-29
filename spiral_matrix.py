class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out = []
        while matrix != []:
            p = matrix.pop(0)
            out.extend(p)
            matrix = list(zip(*matrix)[::-1])
        return (out)
        