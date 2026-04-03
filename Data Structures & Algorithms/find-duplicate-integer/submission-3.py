class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        print(nums[slow], nums[slow2])
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            print(slow2, slow)
            if slow == slow2:
                return slow
        