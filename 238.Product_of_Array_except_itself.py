# from collections import defaultdict
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            if num != 0: prod *= num
        
        arr = []
        filtered = list(filter(lambda x : x == 0, nums))

        if len(filtered) >= 2:
            for i in range(len(nums)):
                arr.append(0)
            return arr
        elif len(filtered) == 1:
            idx = nums.index(0)
            for i in range(len(nums)):
                if i != idx: 
                    arr.append(0)
                else: arr.append(prod)
        else:
            for i in range(len(nums)):
                arr.append(prod // nums[i])
        
        return arr