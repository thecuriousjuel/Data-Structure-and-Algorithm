class Solution:
    def fun(self, s, t):
        dict1 = {}
        
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            if char1 not in dict1:
                dict1[char1] = char2

            elif dict1[char1] != char2:
                return False

        return True
    
    
    def isIsomorphic(self, s: str, t: str) -> bool:

        out1 = self.fun(s, t)        
        out2 = self.fun(t, s)
        
        return out1 and out2

        