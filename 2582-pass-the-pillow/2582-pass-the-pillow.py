class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time + 1
        rem = time % (n-1)
        if time//(n-1) % 2 == 0:   
            return rem + 1
        return n - rem

            
        
        