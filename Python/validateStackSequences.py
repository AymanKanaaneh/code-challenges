#https://leetcode.com/problems/validate-stack-sequences
#Level: Medium
#Time Complexity: O(n), n = len(pushed) = len(popped)
#Space Complexity: O(n), n = len(pushed) = len(popped)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        if len(pushed) != len(popped):
            return False

        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j+=1
        
        return not stack
        