class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            #add all numbers to hashmap
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            #find the other number, by subtracting number and current index
            otherNum = target - nums[i]
            if otherNum in hashmap and hashmap[otherNum] != i:
                return [i, hashmap[otherNum]]

        return []