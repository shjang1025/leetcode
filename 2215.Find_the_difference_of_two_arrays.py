from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        res1 = []
        res2 = []

        for n in nums2:
            if n not in s1 and n not in res2: 
                res2.append(n)
        for n in nums1:
            if n not in s2 and n not in res1:
                res1.append(n)
        return [res1,res2]