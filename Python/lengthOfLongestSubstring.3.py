#https://leetcode.com/problems/longest-common-prefix
#Level: medium
#Time Complexity: O(n*m), n = len(strs), m = redundant letters in s

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeardLetters = {}
        maxSubstrLen = 0
        currentSubstrLen = 0
        i = 0

        while i < len(s):
            if s[i] in appeardLetters:
                maxSubstrLen = max(maxSubstrLen, currentSubstrLen)
                i = appeardLetters[s[i]] + 1
                appeardLetters = {}
                currentSubstrLen = 0
            else:
                appeardLetters[s[i]] = i
                currentSubstrLen += 1
                i += 1

        return max(maxSubstrLen, currentSubstrLen)
    
    

#Level: medium
#Time Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeardLetters = set()
        left = maxLen = 0

        for right in range(len(s)):

            while s[right] in appeardLetters:
                appeardLetters.remove(s[left])
                left += 1

            appeardLetters.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen