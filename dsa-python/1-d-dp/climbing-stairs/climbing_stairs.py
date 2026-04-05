class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one = 2
        two = 1

        for i in range(3, n + 1):
            total = one + two
            two = one
            one = total
        
        return one