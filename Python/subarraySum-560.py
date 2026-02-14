#https://leetcode.com/problems/subarray-sum-equals-k/
#Level: Medium
#Time Complexity: O(n), n = len(nums)
#Space Complexity: O(n), n = len(nums)



class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        currSum = 0
        prefixSum = {}
        prefixSum[currSum] = 1
        numsLen = len(nums)
        count = 0
        diff = 0

        for i in range(numsLen):
            currSum+=nums[i]
            diff = currSum-k

            count+=prefixSum.get(diff, 0)
            
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

            
        return count

        