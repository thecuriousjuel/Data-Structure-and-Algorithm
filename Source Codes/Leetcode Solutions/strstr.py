class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        if len(needle) > len(haystack):
            return -1
        
        if len(haystack) == 1:
            if needle[0] == haystack[0]:
                return 0
            return -1
        
        j = 0        
        ind = -1
        
        for i in range(len(haystack)):
            if j >= len(needle):
                return ind
            
            if haystack[i] == needle[j]:
                if j == 0:
                    ind = i
                j += 1
                
                
            else:
                j = 0
                ind = -1
            
        
        return ind
        