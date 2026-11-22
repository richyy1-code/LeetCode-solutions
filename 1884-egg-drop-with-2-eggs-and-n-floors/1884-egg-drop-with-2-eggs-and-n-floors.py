class Solution:
    def twoEggDrop(self, n: int) -> int:
        lower = int((-1 + (1+(8*n))** 0.5)/2)
        upper = lower + 1
        x = lower - 1
        y = lower
        while x > 0:
            y += x
            x -= 1
        if y >= n:
            return lower
        return upper
        
        

        