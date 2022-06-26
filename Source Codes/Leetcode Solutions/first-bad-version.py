# The isBadVersion API is already defined for you.
def isBadVersion(version: int, bad=1702766719) -> bool:
    return bad == version


class Solution:
    def firstBadVersion(self, n: int) -> int:

        lower = 0
        upper = n-1
        
        while lower <= upper:
            
            mid = (upper + lower) // 2
            
            # print(lower, mid, upper)

            out = isBadVersion(mid)
                
            if out == True:
                upper = mid - 1
            
            if out == False:
                lower = mid + 1
                
        return lower
                
        

s = Solution()
n = 2126753390

print(s.firstBadVersion(n))