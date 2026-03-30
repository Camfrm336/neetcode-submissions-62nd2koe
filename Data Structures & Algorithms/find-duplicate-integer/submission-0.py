class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = set()

        for n in nums:
            if n in hashMap:
                return n
            hashMap.add(n)
        