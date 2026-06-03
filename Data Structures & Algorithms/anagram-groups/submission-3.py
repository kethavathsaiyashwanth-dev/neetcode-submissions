class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # hash_map = {}
            hash_map = defaultdict(list)
            for s in strs:
                key_str = ''.join(sorted(s))
                if key_str not in hash_map:
                    hash_map[key_str] = []
                hash_map[key_str].append(s)

            res = []
            for key_str in hash_map:
                res.append(hash_map[key_str])
            return res