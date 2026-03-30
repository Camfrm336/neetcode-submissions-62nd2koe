class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            print(mid)

            print(mid * mid)
            if mid * mid < x:
                left = mid + 1
                res = mid
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        
        return res


        