class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = int((-1 + (1+(8*n))** 0.5)//2)
        return f if f*(f+1)//2 >= n else f+1
        
        
        

        