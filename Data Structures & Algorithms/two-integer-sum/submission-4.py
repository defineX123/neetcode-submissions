class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = defaultdict(int)

        for i,v in enumerate(nums):
            complement = target - v
            if complement in storage:
                return [storage[complement], i]
            storage[v] = i
        return []
        