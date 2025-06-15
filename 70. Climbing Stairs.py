class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        for i in range(n):
            suma=a+b
            a=b
            b=suma
        return suma