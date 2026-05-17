class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set_list = list(set(nums))
        return len(nums_set_list)<len(nums)