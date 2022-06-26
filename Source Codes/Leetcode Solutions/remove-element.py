class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
                continue
                
            i += 1
                
        return len(nums)
        