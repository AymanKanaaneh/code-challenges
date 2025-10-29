#https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0 or len(strs[0]) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefLen = 1
        c = strs[0][0]
        common = ''

        MAX_INT = 2**31 - 1
        for i in range(0, MAX_INT):

            if i >= len(strs[0]):
                return common

            c = strs[0][i]

            for j in range(0, len(strs)):

                if prefLen-1 == len(strs[j]):
                    return common

                if strs[j][prefLen-1] != c:
                    return common
            
            common+=c
            prefLen+=1
        
        return common