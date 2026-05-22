class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for i in range(len(nums)):
            if nums[i - 1] in new:
                return True
            else:
                new.append(nums[i - 1])
        return False
        