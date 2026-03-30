class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1
        while left < right:
            twoSum = numbers[right] + numbers[left]
            if twoSum == target:
                return [numbers[left], numbers[right]]
            elif twoSum > target:
                right -= 1
            else:
                left += 1
        
        