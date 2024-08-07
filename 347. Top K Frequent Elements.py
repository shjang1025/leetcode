from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        frequent = []

        for num in nums:
            h[num] = 1 + h.get(num, 0)
        for i in range(len(nums) + 1): frequent.append([])

        for num, frequency in h.items():
            frequent[frequency].append(num)
        res = []
        for i in range(len(frequent)-1, -1, -1):
            for num in frequent[i]:
                res.append(num)
                if len(res) == k: return res
        return res