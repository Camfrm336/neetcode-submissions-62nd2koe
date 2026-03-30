class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1

        while True:
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/speed)
            
            if totalTime <= h:
                return speed
            speed += 1
        

        


       
        
        