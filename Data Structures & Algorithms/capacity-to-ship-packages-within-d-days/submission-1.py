class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        print(left,right)
        res = right
        while left <= right:
            cap = (left + right) // 2
            currCap = cap
            day = 1
            for weight in weights:
                if currCap - weight < 0:
                    day += 1
                    currCap = cap
                currCap -= weight
            if day <= days:
                right = cap - 1
                res = min(res, cap)
            else:
                left = cap + 1
            
                 
        return res