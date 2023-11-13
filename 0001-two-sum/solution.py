class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if target == (nums[x] + nums[y]):
                    return (x,y)
                
        
        
