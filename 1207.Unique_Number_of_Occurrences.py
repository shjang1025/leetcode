from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}

        for num in arr:
            h[num] = 1 + h.get(num, 0)
        
        occurrence_set = set()
        for k, v in h.items():
            if v in occurrence_set: return False
            occurrence_set.add(v)
        return True