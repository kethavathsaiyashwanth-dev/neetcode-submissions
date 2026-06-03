class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        pairs = list(hashmap.items())
        pairs.sort(key=lambda x: x[1])
        res = list(map(lambda pair: pair[0], pairs[-k:]))
        return res