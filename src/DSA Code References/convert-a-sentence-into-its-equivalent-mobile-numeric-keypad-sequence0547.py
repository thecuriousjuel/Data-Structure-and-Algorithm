#User function Template for python3

class Solution:

    def printSequence(self,S):
        phone = {}

        count = 1
        num = 2
        for i in range(65, 90+1):
            phone[chr(i)] = str(num) * count
            count+=1
                    
            if num == 7 or num == 9:
                if count == 5:
                    count = 1
                    num += 1
            else:
                if count == 4:
                    count = 1
                    num += 1
                    
        phone[' '] = str(0)
                    
        numpad = ''        
        for i in S:
            numpad += phone[i]
            
            
        return numpad
 
        print(phone)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        inputStr = input()

        solObj = Solution()

        print(solObj.printSequence(inputStr))
# } Driver Code Ends