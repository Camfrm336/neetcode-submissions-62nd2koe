class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCount = 0

        for n in nums:
            count = 1
            num = n
            while num - 1 in nums:
                count += 1
                num -= 1  
            maxCount = max(count, maxCount)
        return maxCount
        