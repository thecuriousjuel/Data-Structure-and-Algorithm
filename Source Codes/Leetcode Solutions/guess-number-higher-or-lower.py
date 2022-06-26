# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        lower = 1
        upper = n

        while lower <= upper:
            mid = (lower + upper) // 2
            
            # print(lower, mid, upper)
            
            
            
            out = guess(mid)
            
            if out > 0:
                lower = mid + 1
                
                
            elif out < 0:
                upper = mid - 1
                
            else:
                return mid
            
            
        