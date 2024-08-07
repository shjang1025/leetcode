from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = defaultdict(list)
        for word in strs:
            srt = ''.join(sorted(word))
            ana_hash[srt].append(word)
        res = []
        for values in ana_hash.values():
            res.append(values)
        return res


solution = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(solution.groupAnagrams(strs))
