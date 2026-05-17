class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            if target-nums[i] in hashmap.keys():
                return sorted([i, hashmap[target-nums[i]]])
            hashmap[nums[i]] = i
        return []
