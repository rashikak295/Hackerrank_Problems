class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def case_combinations(substri,index,S,out):
            if len(S) == index:
                out.append(substri)
            elif S[index].isdigit()== True:
                case_combinations(substri + S[index], index+1,S,out)
            else:
                case_combinations(substri + S[index].lower(), index+1,S,out)
                case_combinations(substri + S[index].upper(), index+1,S,out)
        
        out = []
        case_combinations("",0,S,out)
        return out 
        