class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        res = ""

        while left in range(len(word1)) or right in range(len(word2)):
            res += word1[left] if left in range(len(word1)) else ""
            res += word2[right] if right in range(len(word2)) else ""
            left += 1
            right += 1
        
        return res

        