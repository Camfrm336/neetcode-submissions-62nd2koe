class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float("inf")
        windowSum = 0

        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum > target:
                res = min(res, right - left + 1)
                windowSum -= nums[left]
                left += 1
        
        return res if res != float("inf") else 0
        