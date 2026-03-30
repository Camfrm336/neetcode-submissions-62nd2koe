class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right


        while left <= right:
            k = (left + right) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            if totalTime > h:
                left = k + 1
            elif totalTime <= h:
                right = k - 1
                res = min(res, k)
        return res
        

        


       
        
        