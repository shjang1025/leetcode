from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = -999
        res = [0]
        for g in gain:
            res.append(res[-1] + g)
            mx = max(mx, res[-1])
        return mx
    
solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
