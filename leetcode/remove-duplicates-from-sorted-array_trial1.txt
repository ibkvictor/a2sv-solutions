class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = len(nums) - 1 
        curr = prev - 1
        while curr >= 0:
            if nums[curr] == nums[prev]:
                nums.pop(curr)
            
            prev = curr
            curr -= 1