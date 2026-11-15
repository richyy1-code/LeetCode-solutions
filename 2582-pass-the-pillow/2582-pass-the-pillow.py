class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time + 1
        elif n == time:
            return n - 1
        else:
            rem = time % (n-1)
            if time//(n-1) % 2 == 0:   
                return rem + 1
            else:
                return n - rem

            
        
        