class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxF = 0
        res = 0
# ABAB
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxF = max(maxF, count[s[right]])
            windowSize = right - left + 1
            while windowSize - maxF > k:
                count[s[left]] -= 1
                left += 1
                windowSize = right - left + 1

            res = max(windowSize, res)
        return res
        