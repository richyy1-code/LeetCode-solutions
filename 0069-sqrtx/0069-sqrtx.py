class Solution:
    def mySqrt(self, x: int) -> int:
        done = False
        min = 0
        max = x
        count = 0
        while not done:
            value = (max + min)/2
            answer = value * value
            if answer < x:
                min = value
            elif answer > x:
                max = value
            else:
                return int(value)
            count += 1
            if count == 100:
                done = True
        return int(value)
        