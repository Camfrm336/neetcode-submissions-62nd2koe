class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = defaultdict(int)
        res = 0
        total = 0

        for i in range(len(fruits)):
            count[fruits[i]] += 1
            total += 1
            while len(count) > 2:
                fruit = fruits[left]
                total -= 1
                count[fruits[left]] -= 1
                left += 1

                if not count[fruit]:
                    count.pop(fruit)
                
            
            
            res = max(res, total)
        
        return res

        