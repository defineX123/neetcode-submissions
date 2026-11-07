class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in range(len(nums)):
            if nums[num] in x:
                return True
            else: 
                x.add(nums[num])
        return False     