class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n > time:
            return time +1
        elif n == time:
            return n - 1
        else:
            if n == 2:
                if time % 2 == 1:
                    return 2
                else:
                    return 1
            elif time//(n-1) % 2 == 0:
                rem = time % (n-1)
                return rem + 1
            else:
                rem = time % (n-1)
                return n - rem

            
        
        