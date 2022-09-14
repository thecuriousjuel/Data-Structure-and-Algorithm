class Solution:
    
    # This function extracts the digits, squares them and return them back
    def fun(self, n):
        s = 0
        while n > 0:
            d = n % 10
            s = s + d ** 2
            n = n // 10
        
        return s
        
    def isHappy(self, n: int) -> bool:
        
        # Arbitrarily to prevent the program from entering endless loop,
        # I used a counter. The counter will count till 10 steps.
        # If the program is still not able to produce 1 after 10 steps
        # it ends. 
        count = 0
        while count < 10:
            n = self.fun(n)
            if n == 1:
                return True

            count += 1
            
        return False
            
        