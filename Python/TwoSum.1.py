class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsSubTarget = [0] * len(nums)
        numDic = {}

        for i in range(0, len(nums)):
            numsSubTarget[i] = target - nums[i]
            numDic[nums[i]] = i
        
        for i in range(0, len(nums)):
            if numsSubTarget[i] in numDic and numDic[numsSubTarget[i]] != i:
                return [i, numDic[numsSubTarget[i]]]

        return [0, 0]
        