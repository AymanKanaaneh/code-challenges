class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strsLen = len(strs)
        strsArr = [""] * strsLen
        anagramsG = []

        for i in range(strsLen):
            charArr = sorted(strs[i])
            strsArr[i] = ("".join(charArr), i)

        strsArr.sort(key=lambda x: x[0])

        i = 0
        while i < strsLen:
            anagram = []
            while i < strsLen - 1 and strsArr[i][0] == strsArr[i+1][0]:
                anagram.append(strs[strsArr[i][1]])
                i += 1

            anagram.append(strs[strsArr[i][1]])
            anagramsG.append(anagram)
            i += 1 

        return anagramsG
