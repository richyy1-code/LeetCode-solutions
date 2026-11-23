class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = (-1 + isqrt(1+8*n))//2
        return f if f*(f+1)//2 >= n else f+1
        
        
        

        