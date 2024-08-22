# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            num = i*i
            if num == x:
                return i
            elif num > x:
                return i-1
        return x    
        
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(2))